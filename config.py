# API Keys
GOOGLE_MAPS_API_KEY = "AIzaSyCNcx0fpjrGqOMZOMnqoYt_oqHYXuDRzfA"
OPENWEATHER_API_KEY = "1c2ccfd168a2fb4ce1ecaeb0218eeb56"

# Google Sheets
SHEET_ID = "1v1Ai0PmvAPTs4F4IsbQMeMM75xz9SydZczmf5C7S-9Y"
SERVICE_ACCOUNT_FILE = "traffic-analysis-486814-015f63b18402.json"

# Addresses - Using coordinates directly
HOME_COORDS = "38.679603,-9.318898"
OFFICE_COORDS = "38.771227,-9.109578"

# Multiple Routes - Home to Office
# Add as many routes as you want! Each route needs a name and polyline.
HOME_TO_OFFICE_ROUTES = [
    {
        "name": "Preferred",  # Change this to whatever you want
        "polyline": "qrakFdb{w@uBw@_@[q@u@s@jAiAJCo@@oAJ_ALk@T[LQHGDMCMB[HWPi@?UGk@M[]WiAY_@E_@@IJQFM?[Gs@m@eCcCuDqDgDeDu@gAo@{A[mAQwAEwAFyCJuD?iBYqE_AuF{AcIkAeG_@qAy@aBi@w@m@o@sCaCcBwAq@u@k@s@gBcDgCiGg@iBeBmHoAqFwBiGqBuFg@kA_AaAwAm@kAg@m@g@]c@eCuE{BoE]}ASsCMsAg@kBqBsDe@_BM_AWqEQ_B]kAQa@[g@uAiBs@cA]q@Sq@WwAWiH?yCL{EVcIb@_NNqA`@uAf@{ALq@D{@Cq@Ky@yBoHs@{Cg@uCQcAKuAEeBM{COkAyA_JcAmFMaAC}@V_Dh@_FIk@WY]HoA?aD\{@TkBr@kGnCuBnAcFpDkE|CeBr@}A\mAFaD@g@@gACQGo@Gw@OcAi@uAuAqA{AeAiAm@e@qEiBg@[g@e@]e@i@_BQ_CMu@@kGCwDKiCSyBm@uC}@wCkAcCeA_B{@_AcB}AkDkC_HiFoBgB_AgAkBmCu@{AsAeDaAwDu@qE[cFC_EDiBPgEj@_EdA}DrJgXvBoG`AeDdAmEr@oDf@oDR{A`@{EVkFHaEAmH[oKCq@OuDEaAFgBFkALsAJ_ALyAEwACSOq@Wk@g@k@a@Y{@i@oDuBcAs@e@g@y@_BCGOCCGEM}@_Cg@qA_BgEgFeNkByEoAoCmBsCkBgB}BqA}Ag@uB]yAGaBDqBZw@JuAf@yDpA{Bh@wALmBHiBQqBi@}BeAaCqAqSkL}EiC{KgGMWc@Ue@YOUa@iAQmAW}@Ua@c@_@wBeAY_@Qu@KwBEi@OKEw@MmAWqA]gAs@uAe@o@{D_EuJuJo@}@o@kAm@eBe@wBgByIs@gD}@{Cy@}Ak@w@_AcAkBkAiBs@}Bs@cHyBwB{@iCuA_CyA{DeDyC_DqCuD{CoFeB}D{AiEyAuFc@uBo@_E]}CW_DOgDEwFHkHVaN\oRLkKEgDKeCg@aG}AoKkBiMiCkQcAoG_AaEw@{CmAgFmBiHaCcLM_AkA_Js@sGqAsM_@cHSyHA}DFeLFcREeEQmDGq@m@}DgA}DcAiCkB}Ci@q@cAiAw@{@c@y@[]o@y@]]GWaAy@kA}@k@a@uA_AuC}AgBu@uAe@AM?ASOQWGG@_@?]EKXoGj@wK^_FLmCJkFLaBYoBE[IYO_EG}@Gu@q@aG}@gFo@}CWkBOeESiA]c@UMk@_@[@OPM`@V|@BZCLU`@YL"
    },
    {
        "name": "Preferred e Alges",  # Change this to whatever you want
        "polyline": "qrakFdb{w@uBw@_@[q@u@s@jAiAJCo@@oAJ_ALk@T[LQHGDMCMB[HWPi@?UGk@M[]WiAY_@E_@@IJQFM?[Gs@m@eCcCuDqDgDeDu@gAo@{A[mAQwAEwAFyCJuD?iBYqE_AuF{AcIkAeG_@qAy@aBi@w@m@o@sCaCcBwAq@u@k@s@gBcDgCiGg@iBeBmHoAqFwBiGqBuFg@kA_AaAwAm@kAg@m@g@]c@eCuE{BoE]}ASsCMsAg@kBqBsDe@_BM_AWqEQ_B]kAQa@[g@uAiBs@cA]q@Sq@WwAWiH?yCL{EVcIb@_NNqA`@uAf@{ALq@D{@Cq@Ky@yBoHs@{Cg@uCQcAKuAEeBM{COkAyA_JcAmFMaAC}@V_Dh@_F?yAIs@k@yBk@iCEy@?eCEyBYmAUq@_@k@mBsC]cAQeAKcA?cAReE\aCVi@hCiEjCmEf@}APcAHcBz@a]hAmb@p@aSAcMAkFHwER}CVyBZaBdAyEl@eBBIUQYYmAu@i@QW@c@PQHOPm@f@SFqBPQ?wBI}Du@iBc@SBqAc@iBq@}CeBy@k@kAcA}@aAiD{DgBgBiA{@uAu@sBw@uA_@oBWkCKkDN_Gb@uCFcACyAMoAKw@QyBo@sAk@e@_@[SsAu@wDyCgCkBw@s@eBcBiA}Aq@mAw@gByAyD}AaEaEsK{DcKoAoCmBsCkBgByA{@mAi@}Aa@aCUwA?yAJwAVaB`@iBp@sBp@u@TiARwBL_ADuAKi@IsCaAe]kRgDgB{GyDm@Y[QKUUMe@WSOWc@YiAUsASm@Ya@iAs@}@a@SQ]q@Im@KgCQQOmBM}@Qs@a@oAm@iAy@cAaAaAoImIcBcBo@u@q@aAo@sAk@iBoAeGuBcKgAwCyAyByAuAaB}@_DeA_D_AmEyAgCgAeCwAsBuAcBuA}CyCqDuE}CkF{AcDgAsCw@_Cq@eC_A}D_@yBg@yDYaD]{HAsDH}GLmGPmJP{JPqKAyDIuCa@oFuA_KyBcOkCqQo@mEq@cDqAiFcAkEwAqFsCcMc@gCa@qCkCoU{@_LYwHG{G@aEDyJDqRSiF]uCY_Bi@uBaAsC}A{CeA}AmCyCc@y@GIq@y@a@c@Ue@cDiCuA_AeCwAoB}@sBs@AOIE[a@GG@_@?]EKFgA|@_R^_FH}AN{GLaBIq@UyAIYO_EG}@]sDcA{GeAiFSsAIsAIiCOgAWa@UO_@UUOU?KDGHELIVHVPn@?TWh@[N"
    },
    {
        "name": "CREL e Jamor",  # Add a second route
        "polyline": "qrakFdb{w@uCsAq@u@s@jAiAJCo@@oAJ_ALk@T[LQHG@[^sBUgA]WiAY_@Ei@L_@FoAu@{HuHgDeDu@gAo@{A[mAWoDRyLYqE_AuF{AcIkBwIcByCaEqDuCmCk@s@gBcDgCiGmCwKoAqFwBiGyCaI_AaAwAm@kAg@m@g@cDyF{BoE]}ASsCMsAg@kBqBsDe@_Be@qGQ_Bo@mBqBqCqAuBk@iCWiHLuJVcIb@_NNqA`@uAt@mCD{@OkByBoH{AqH]yCEeBM{COkA}CmQQ_CV_Dh@_FIk@WYmBH}Er@kBr@kGnCyI`GkE|CeBr@}A\mAFaD@oBAyB_@cAi@uAuAqA{AsBoBqEiBoAaA]e@i@_BQ_CMu@AcM_@cGm@uC}@wCkAcCaC_DoGiF_HiFoDoDkBmCu@{AsAeDaAwDu@qE[cF@iHPgEr@yEpAmEjJwW|BaH|@_D`BsHhAiId@_GRyFFaEGuHWgISyEDwE\yDLaBGmAIi@q@{A}B_BqDwBeB{Au@}AOC_@aAyA{D_BgEgGePuAgDmBsDcBwBmAeAwBiA}Ag@{B]oCCkEj@iHdCiCd@}CNkC[mEeByMuHyTwL{EoCaBs@eEw@gBGmEPcD\y@TyAn@{CxB{FtG_A~@}EvDoFvDuFvD{At@uBh@cBHsBOeASuAm@sFeDkU}NuAu@_AYsBKyAHeBb@iBdAiMtKyFzEkAp@oBn@mAJiBCqB_@yCaAoFkBuCsAwCsBuC}CeC_Eo@uAiBcFyE{OeF{PgBqF_CcEwCoCuBkAoIoE}BaBsAmAmDqEoBsDeB}EcByHkByL{@aDmDwJcA{E_BcRw@iJWaBs@gCk@uAkAoB{AiBkFwFaBuCs@qBeGkSuAcD}@cAeAq@_A[sCa@qC[o@KuAi@mA}@gBgCc@c@u@yAaA{BmAkDuA_FgBoJ}AiHmAwDAq@kA_Fw@cLu@yEoAeDmA_BqC_CcCqBwBuCiDuFkFyEuCgDiAsBg@yA[yAk@yEKqHFkGVyFjA{Op@oFvAkInAeG~BgLpAuIrB_PfAoIp@iDv@{BzAqCzHoKfAsBz@uB|A}EnAkFV}@bB_F|@_BnAiAnEkD`AUlGo@bA@dCt@dCd@fAKfAs@n@eAVsA?cCG_DNwAb@sA`BuCzFgK~EsLl@kAbAkAhBgA`C_AvCoBnCiA|Bc@`@UtD]rCAjCHr@XpEX~CD|LH|@N`@JnBMjBMn@TZNt@v@`E`G~@lBd@xAv@vCGh@k@d@"
    },
    # Add more routes here by copying the pattern above
    # {
    #     "name": "Route 3",
    #     "polyline": "YOUR_THIRD_POLYLINE_HERE"
    # },
]

# Multiple Routes - Office to Home
OFFICE_TO_HOME_ROUTES = [
    {
        "name": "Preferred",
        "polyline": "coskF`frv@XMR?h@Lz@vA|@lBJf@P`@l@lC|@fFv@nHXdGDhHGfFYlGA`Ak@vKYnGGLEj@ObCC~@Y|D@b@Jd@Xd@\Tf@BVKVWVYx@aAn@i@f@Kd@@dAZ|Aj@PJLEzBhBr@p@xEbFn@x@lAfBfArB`ArCp@nC`@tBXzCH|B@fEG`RChC?~JJtGZzH`@nFz@nItB~Pp@fEjBhI~AlGnChLvAvG`AvGlChQxClSb@hDJlATjDFzB?fHEdBc@`Uc@pVFpGH|@LjCt@xHpAdIb@bBbArDdAzC`ClFn@jAvBjDvCvDjBjBtApAjA~@tAbAbDlB`CbAnEzAhHzBvAl@|AbAl@j@h@bAfA|BfAjE~CjOr@xBn@nAd@r@vDzDpGnGjCpCt@nAZt@ZnANlATdFZlKNhENtBYdBIVSTa@R_@Bg@Y[o@KwA@w@Fi@Ne@Xe@l@Y~AG~A?RGlBT~Ab@zBbAdDfBfDjBxC|AjLpGjH~DlFnCpBj@rC`@jA@bBKp@K`Ba@tAa@nFgBnB]x@EdCFhANlA\`A^|A|@~AtAnA~AnAxB~ApDlElLjGlPpBvEnAnBhArABXz@pAf@bAr@jBZlA^fCD\P^D|AFpABf@JtCBl@VhHFvGIfGSbFUxCm@rFkAbHk@hCm@`CoA`E}@jC{@`CeH~RcBdGUjA[tBUzBO~CC|DPnEl@bFx@zDj@jBxAnDpBfDr@|@|A|A|CfCrFfEnEnDfBtBl@~@~@nBbAvCXjA\zBP|BD|BK|LEtGGzDWzEi@nD{@rDq@pBg@j@c@dAwAzCi@nBs@|C_@xBu@dEMb@QR_@LY@[IQQOYGm@D_@Vi@Xm@rDkCfBmAlIgGpKqHtBwAzAw@x@]bA_@hASlBMdGGz@Ap@InA]|@g@bA{@zEkDlDgCtBoAhBy@lGiCz@U`D]nA?NLV\FN?ZKz@k@vEGrADrAbB`JnAzHRxCF`CD|@h@rDh@vC\lA|AdF^rAD`@@~AO`Ay@fC]pB_@hLg@~PErBFtCPvER~AZ`Ap@jAdCjDf@lA\bBXtENxAb@~Ar@tAr@jAf@vAVpB\`E\fA~@nBxAnCjBhDp@t@TRz@`@`Bl@z@v@n@rAvE|MfAhEjArFbA|DTv@v@lBnAnCjAbCzAnBnApA~AlAx@l@`B|AZb@z@`Bj@jB~DhTf@rDJdBDvCUtHBlBNzAXnA`@dAf@dAd@j@rCpCjIhI|CzBnChB`G|DLX?PGVMZRLJFn@Pb@Ni@hDyEsARmAtBv@"
    },
    {
        "name": "Alges",
        "polyline": "coskF`frv@XMR?h@Lz@vA|@lBJf@P`@l@lC|@fFj@vEJvAXdGFrDAtBGfFYlGA`Ak@vKYnGGLEj@Gn@GrAC~@Y|D@b@Jd@Xd@\Tf@BVKVWVYx@aAVYVOf@Kd@@dAZ|Aj@PJLEzBhBr@p@xEbFn@x@lAfBfArB`ArCp@nC`@tBXzCH|B@fEG`RChC?~JJtGZzH`@nFz@nIfAfJl@vEp@fEjBhI~AlGnChLt@bD`@rB`AvGlChQxClSb@hDJlATjDFzBB|BChDEdB_@xQe@jWApDDjDJ~@FrA\~EVvBVlBrAhHjAhEv@dCbAbC`AtBhCvExCbEzBbC|BvBdChBrBpAfCpAdAb@~CdAlErAxAb@nBv@~AdAh@^h@r@jA`Cx@nCfDfP^~A`@lAd@bAp@dAfAnAtAtAnGjGxC|Cx@jAb@`AZlAPjAVrFPfFV~HD`BLdAUxAI\ORWTe@HYCOKSSMYMiAA_ABg@Le@Ri@LO\S`@Id@C~B?PG|ANfBb@lAb@xEdChCvAlBbAvLvGhP~InCdArCd@dBB~@ChAOtAYvAc@~EaBhBc@hAK|@AdBDb@Dp@LZFzAj@vAt@x@l@`BdBt@fAh@`Ad@z@bA~B|BbGjA~ClGlPnBxE|@`B|@nAbC~BfA|@dBjArD`D\T|@h@fB`AxBx@`Cf@l@Jz@HtCB`CGvDUxDWZAn@@xADn@HvB`@~Aj@x@\lBdAjA`ArDvDrBzBh@f@rA`A|@j@bBdAbDfALNnC`AbCp@^FdBPT@dCG~AS~AQTAZHTTNd@B\o@vDSvA?f@WxBS|CIvED`RCdCe@zLk@`RaAla@a@nOEfAIt@]tAa@`A}AhCsDhGQd@Kl@SjBIdBGfABpA^|B^`AfA~Aj@x@Zj@Pj@F~@DjA?jDBt@Jv@^fBPrCBtBQlBYjCAxAD~@Jp@xA~H`A~FVdBPzANnF\lCh@`Dd@hBl@pBt@~Bb@fBDzAGv@Sz@}@vCGZKrACj@SpGIvCe@|PB`CPvFN|AXfA^t@`B|BlAlBd@vATjB\lFPz@Nh@l@nAr@jAj@tA\~APrCJbADTd@zApBxDpBtDz@jATRt@d@dBl@VLf@b@\j@bDxIfBnFdAvEnAvFz@bDx@rBpArCdAvBV`@rBfCdCpBVRfBxAj@n@|@|An@lBfBlJhBvJTdBPlBFbCElCMxDC~@DjAHbAXxA\fAj@jA^h@lAlAlEhEvDvDrAjAbMlIn@`@HNDRWz@\RNBdA^i@hDyEsARmAtBv@"
    },
    {
        "name": "CREL e Alges",
        "polyline": "coskF`frv@l@Mh@Lz@vA\CRU?kBOgAm@q@yAgAuAgBsBaDwDuFOU[uAKq@i@a@cEPa@Dc@\EN[@wC@}IEcCCgAAk@NgBMyBMwCAsAHgA?qAC_Cc@y@?{@Zq@~@{@~AmAjBu@h@qFtBuFrBi@~@m@tDqA~FaB|CmBjCoAt@{Br@{@p@_AzAy@tA}AdBoBlB}E`DqFtDmClCm@|@k@tAs@|As@nB_ApDmAxEoBtFaCrE{EhG_CtD_AbCeArEo@zEwBvPsAjJmDzQeB`JwA~Iw@fIo@hNE`IHfGJ`Br@xDp@xBpA~BnDxDtCfCjAjApApB|BvDzBdCrDpCvA~Av@pAfAnDd@|CHfCCbCBfFf@zC|AlDnAlCTTVjAbAzFx@fEjBvGrApDfBvDrC`F`BtBrD`ErAz@hA^nDz@tAf@xBfB|@vArAfEdAhDtB`FvAlB|CfDdBpB|B~Dd@xAl@|Cx@pJnAlO|@tF|AvElBjFnArFtAjJfAlFzBtGhCvEpDnExAnAlFdDnG~CdDhCdC|DvA~DpBzGxCfK`DvKlBvFlC~F|BdDnDfDvA|@bEhB~G`ClBn@~ATpCCxAYv@YtCoB`EuDrJkIbCeBfAa@`De@zAJ`Bl@dJzFbSdMhC~@zBZhBCfB[pAc@nCaBdJsGvFaEpCoCnG_HzByAnA_@tFg@hBEpBFlBT~Ab@`HjDfDjBlLlGbM`HlFnCpBj@rC`@l@@`CKrCm@dIiChDc@nEVnC|@|A|@~AtAnA~AnAxBf@hA~B|FfBzElFjNbChG|@hBvAtBjE|DvHbGfFlCvEfAdAJ`CFdFQvHe@r@?pCNjDx@dA`@rAn@dCfBbIlIxCvBv@f@bBx@pBn@HJDDpGpBnCZdA?fCStASpACl@j@DhA_AxFIvAi@zI@hM?xHSbGo@zRaAb`@w@fZg@jCcAtB{E`Im@vA]nDKfDZnCVbAh@|@bBdCZr@NrAFvG\|BTzANdF]fDQzCJbB~BbMhA|HPzFbAdHrAdFzAhFHhAQxBkAbEQ~B]~Kg@~PRxJHtAZrAbBzCjBlCf@rAV~AZdFTzAr@hB`B|C\tAPhBNzBd@jB~D~HdBjCf@f@lBt@jAl@j@v@~AbEnDdK~@`EnCjLjCnGp@vAzBbDvDdDrCdC~@vAn@bBtAdHrCrOV~BJtCA~BSjH^~DdArCbAvAdF`FdHzG~HlFvDdCLXGh@MZRLJFn@Pb@Ni@hDyEsARmAtBv@"
    },
    {
        "name": "CREL e Jamor",
        "polyline": "coskF`frv@l@Mh@Lz@vA\CRU?kBOgAm@q@yAgAuAgBsBaDwDuFOU[uAKq@i@a@cEPa@Dc@\EN[@wC@}IEcCCsBLaF[wCAsAHgA?qAC_Cc@y@?{@ZmB~CmAjBu@h@gNhFi@~@m@tDqA~FaB|CmBjCoAt@{Br@{@p@_AzAy@tA}AdBoBlBoMvImClCm@|@k@tAs@|As@nB_ApDmAxEoBtFaCrE{EhG_CtD_AbCeArEo@zEwBvPsAjJmDzQ}D`Uw@fIo@hNE`IHfGJ`Br@xDp@xBpA~BnDxDtCfCjAjApApB|BvDzBdCrDpCvA~Av@pAfAnDd@|CHfCCbCBfFf@zC|AlDnAlCTTVjAbAzFx@fEjBvGrApDfBvDrC`FtGvHrAz@hA^nDz@tAf@xBfB|@vArAfEdAhDtB`FvAlB|CfDdBpB|B~Dd@xAl@|Cx@pJnAlO|@tF|AvElBjFnArFtAjJfAlFzBtGhCvEpDnExAnAlFdDnG~CdDhCdC|DvA~DpBzGxCfKnGnSlC~F|BdDnDfDvA|@bEhB~G`ClBn@~ATpCCpCs@tCoB`EuDrJkIbCeBfAa@`De@zAJ`Bl@dJzFbSdMhC~@zBZhBCfB[pAc@nCaBdJsGvFaEpCoCnG_HzByAnA_@tFg@hBEpBFlBT~Ab@`HjDfDjBlLlGbM`HlFnCpBj@rC`@l@@`CKrCm@dIiChDc@nEVnC|@|A|@~AtAnA~AnAxBf@hA~B|FfBzElFjNbChG|@hBvAtBl@n@BX?@dA~Ax@fBz@dDXzBTh@D|ATvFBh@XzHFjJe@dNiAdKwB|K_ElMqEfMcC~GgBrGo@hEc@tIFdE\pEv@`FdAvDtB~EhBrC|CbDtCzBrIvGhC~BnA`BnBfEnAvEf@xF@|EKxNItGq@`Iu@pDcAnDm@p@mArCcAlCo@xBe@hCu@hEYvAc@f@a@Hq@QWg@E{@^}@Ti@dD_Cp@e@dBmAzLyIlHgFlDsBrBu@lBYrEMrEI|@QnAg@pDsCdCeBhImFtGsCrAc@r@OvEYXLX`@Bp@y@xGC|Ad@fDnCdP\~F\fEhAfG~AfFn@~BHhAQxBkAbE]fHi@rQOjI\fJv@jCvCdEn@lA`@dBd@pG\nB~A`Dl@pA\tA`@dFd@jBjBvDrAfCdBjCf@f@lBt@jAl@j@v@xErMtAvElArFxBpIdDlHzBbD`DrChDvC~@vAn@bBhFxXb@tGQrHDxEn@`DnAbC|L|LlBbBlExCpBrAvDdCLXGh@MZRLJFn@Pb@Ni@hDyEsARmAtBv@"
    },
    # Add more routes here
]

# Schedule Configuration
MORNING_START = "06:30"
MORNING_END = "12:30"
EVENING_START = "15:00"
EVENING_END = "20:00"
CHECK_INTERVAL_MINUTES = 15
