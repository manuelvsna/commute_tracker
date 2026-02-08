import googlemaps
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime
import time
import schedule
import config

# Initialize Google Maps client
gmaps = googlemaps.Client(key=config.GOOGLE_MAPS_API_KEY)

# Initialize Google Sheets client
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    config.SERVICE_ACCOUNT_FILE, scope)
sheets_client = gspread.authorize(creds)
sheet = sheets_client.open_by_key(config.SHEET_ID).sheet1

# Setup sheet headers if needed
def setup_sheet():
    try:
        headers = sheet.row_values(1)
        if not headers:
            sheet.append_row([
                'Timestamp',
                'Date',
                'Time',
                'Direction',
                'Route',
                'Duration (min)',
                'Duration in Traffic (min)',
                'Distance (km)',
                'Weather Condition',
                'Rain (mm/h)',
                'Temperature (°C)',
                'Polyline'
            ])
            print("✓ Sheet headers created")
    except Exception as e:
        print(f"Error setting up sheet: {e}")

# Get weather data
def get_weather(coords):
    try:
        lat, lng = coords.split(',')
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'lat': lat,
            'lon': lng,
            'appid': config.OPENWEATHER_API_KEY,
            'units': 'metric'
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        weather_condition = data['weather'][0]['main']
        temperature = data['main']['temp']
        
        # Get rain data (mm in last hour)
        rain = 0
        if 'rain' in data:
            rain = data['rain'].get('1h', 0)
        
        return weather_condition, rain, temperature
    except Exception as e:
        print(f"Error getting weather: {e}")
        return "Unknown", 0, 0

# Decode polyline - standalone implementation
def decode_polyline(polyline_str):
    """Decode a polyline string into a list of lat/lng coordinate dictionaries"""
    coordinates = []
    index = 0
    lat = 0
    lng = 0
    
    while index < len(polyline_str):
        # Decode latitude
        result = 0
        shift = 0
        while True:
            b = ord(polyline_str[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20:
                break
        dlat = ~(result >> 1) if (result & 1) else (result >> 1)
        lat += dlat
        
        # Decode longitude
        result = 0
        shift = 0
        while True:
            b = ord(polyline_str[index]) - 63
            index += 1
            result |= (b & 0x1f) << shift
            shift += 5
            if b < 0x20:
                break
        dlng = ~(result >> 1) if (result & 1) else (result >> 1)
        lng += dlng
        
        coordinates.append({
            'lat': lat / 1e5,
            'lng': lng / 1e5
        })
    
    return coordinates

# Calculate distance from polyline
def calculate_distance_from_polyline(polyline_str):
    """Calculate approximate distance from polyline coordinates using Haversine formula"""
    from math import radians, cos, sin, asin, sqrt
    
    # Decode polyline using our standalone decoder
    coords = decode_polyline(polyline_str)
    
    def haversine(lon1, lat1, lon2, lat2):
        # Haversine formula for distance between two points on Earth
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        km = 6371 * c  # Earth's radius in kilometers
        return km
    
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += haversine(
            coords[i]['lng'], coords[i]['lat'],
            coords[i+1]['lng'], coords[i+1]['lat']
        )
    
    return total_distance

# Get traffic data for route
def get_traffic_for_route(origin_coords, dest_coords, polyline_str, route_name, direction):
    try:
        now = datetime.now()
        
        # Decode the polyline to get route points
        route_points = decode_polyline(polyline_str)
        
        # Extract waypoints from the polyline (sample points along the route)
        # We'll take points at roughly equal intervals to guide Google along our route
        num_waypoints = min(8, len(route_points) // 10)  # Max 8 waypoints (API limit is 25, but we'll be conservative)
        
        if num_waypoints > 0:
            step = len(route_points) // (num_waypoints + 1)
            waypoints = []
            for i in range(1, num_waypoints + 1):
                idx = i * step
                if idx < len(route_points):
                    point = route_points[idx]
                    waypoints.append(f"{point['lat']},{point['lng']}")
        else:
            waypoints = []
        
        # Get directions with waypoints to follow our polyline more closely
        directions = gmaps.directions(
            origin_coords,
            dest_coords,
            waypoints=waypoints if waypoints else None,
            mode="driving",
            departure_time=now,
            traffic_model="best_guess"
        )
        
        if not directions:
            print(f"✗ No directions found for {direction} - {route_name}")
            return
        
        route = directions[0]
        
        # Sum up all legs (since we have waypoints, there are multiple legs)
        total_duration_normal = 0
        total_duration_traffic = 0
        
        for leg in route['legs']:
            total_duration_normal += leg['duration']['value']
            total_duration_traffic += leg.get('duration_in_traffic', {}).get('value', leg['duration']['value'])
        
        # Convert to minutes
        duration_normal = total_duration_normal / 60
        duration_traffic = total_duration_traffic / 60
        
        # Use our precise polyline distance
        distance = calculate_distance_from_polyline(polyline_str)
        
        # Get weather at origin
        weather_condition, rain, temperature = get_weather(origin_coords)
        
        # Prepare data for sheet
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        date = now.strftime('%Y-%m-%d')
        time_only = now.strftime('%H:%M')
        
        # Append to sheet
        sheet.append_row([
            timestamp,
            date,
            time_only,
            direction,
            route_name,
            round(duration_normal, 1),
            round(duration_traffic, 1),
            round(distance, 2),
            weather_condition,
            rain,
            round(temperature, 1),
            polyline_str
        ])
        
        print(f"✓ {time_only} | {direction} | {route_name} | {duration_traffic:.1f} min ({distance:.1f} km) | {weather_condition} | {rain}mm/h")
        
    except Exception as e:
        print(f"✗ Error ({route_name}): {e}")
        import traceback
        traceback.print_exc()

# Main collection function
def collect_data():
    current_time = datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    current_weekday = current_time.weekday()  # Monday=0, Sunday=6
    
    # Only run on weekdays (Monday-Friday)
    if current_weekday >= 5:  # Saturday=5, Sunday=6
        print(f"⏸ Weekend - skipping (today is {current_time.strftime('%A')})")
        return
    
    # Convert time to minutes since midnight
    current_time_minutes = current_hour * 60 + current_minute
    morning_start = 6 * 60 + 30 # 6:30 AM
    morning_end = 12 * 60 + 30  # 12:30 PM
    evening_start = 15 * 60  # 3:00 PM
    evening_end = 20 * 60  # 9:00 PM
    
    # Morning window: Home to Office - CHECK ALL ROUTES
    if morning_start <= current_time_minutes <= morning_end:
        for route in config.HOME_TO_OFFICE_ROUTES:
            get_traffic_for_route(
                config.HOME_COORDS,
                config.OFFICE_COORDS,
                route['polyline'],
                route['name'],
                "Home → Office"
            )
            # Small delay between routes to avoid rate limiting
            time.sleep(1)
    
    # Evening window: Office to Home - CHECK ALL ROUTES
    elif evening_start <= current_time_minutes <= evening_end:
        for route in config.OFFICE_TO_HOME_ROUTES:
            get_traffic_for_route(
                config.OFFICE_COORDS,
                config.HOME_COORDS,
                route['polyline'],
                route['name'],
                "Office → Home"
            )
            # Small delay between routes to avoid rate limiting
            time.sleep(1)
    else:
        print(f"⏸ Outside tracking windows (current time: {current_time.strftime('%H:%M')})")

# Initialize
print("=" * 70)
print("COMMUTE TRACKER - MULTI-ROUTE MODE")
print("=" * 70)
setup_sheet()

# Validate routes and show info
try:
    print(f"\n📍 Locations:")
    print(f"  Home: {config.HOME_COORDS}")
    print(f"  Office: {config.OFFICE_COORDS}")
    
    print(f"\n🛣️  Home → Office Routes:")
    for route in config.HOME_TO_OFFICE_ROUTES:
        distance = calculate_distance_from_polyline(route['polyline'])
        print(f"  • {route['name']}: {distance:.2f} km")
    
    print(f"\n🛣️  Office → Home Routes:")
    for route in config.OFFICE_TO_HOME_ROUTES:
        distance = calculate_distance_from_polyline(route['polyline'])
        print(f"  • {route['name']}: {distance:.2f} km")
        
except Exception as e:
    print(f"\n✗ Error loading routes: {e}")
    print("Check your config.py file!")
    exit(1)

# Schedule the job
schedule.every(15).minutes.do(collect_data)

print(f"\n⏰ Schedule:")
print("  Morning: 6:00 AM - 12:30 PM (Home → Office)")
print("  Evening: 2:00 PM - 9:00 PM (Office → Home)")
print("  Interval: Every 15 minutes")
print(f"\n📊 Logging to: Google Sheets")
print("=" * 70)
print("\nRunning initial test...\n")

# Run once immediately to test
collect_data()

print("\n✓ Tracker is now running. Press Ctrl+C to stop.\n")

# Keep running
while True:
    schedule.run_pending()
    time.sleep(60)