import requests
from redfin import Redfin
import json
import asyncio


client = Redfin()
url = "https://www.redfin.com/stingray/api/home/details/belowTheFold"

querystring = {"accessLevel": "1", "propertyId": "4208613", "pageType": "3"}

payload = ""
'''
client.headers = {
    "cookie": "RF_BID_UPDATED=1;RF_BROWSER_ID=AC5Ykvq-SlqOMjvLWTbk8Q;RF_BROWSER_ID_GREAT_FIRST_VISIT_TIMESTAMP=2025-02-26T13%3A15%3A49.398343;RF_ACCESS_LEVEL=3;RF_AUTH=8bcbb03afcc32a0fa723f2feba1c4be5815f7dbd;RF_LAST_USER_ACTION=1740604615978%3A5b1dae361a6d60594361f6d477ca61dd60cab7ba;RF_PARTY_ID=86052287;RF_SECURE_AUTH=4131a21d3ea87fc2a2059256c3356da906020888;RF_W_AUTH=8bcbb03afcc32a0fa723f2feba1c4be5815f7dbd;RF_LAST_ACCESS=1740620421945%3Ab99ccb24f9892d7466e49c3376578504ba24ef17;AMP_TOKEN=%24NOT_FOUND;PageCount=5;RF_LISTING_VIEWS=198378522.195772397.197076500.197189908.197173895.197273654;OptanonAlertBoxClosed=2025-03-03T14:29:06.883Z;OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+03+2025+09%3A29%3A06+GMT-0500+(Eastern+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=65b459a7-8378-4ce1-99e5-e82096b71748&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=US%3BNC;_ga=GA1.2.946058524.1740604551;_ga_928P0PZ00X=GS1.1.1741011664.7.1.1741012146.60.0.0;_gcl_au=1.1.49758447.1740604551;_gid=GA1.2.451037982.1740936512;_scor_uid=5f5f98149b7542c1b64a3e87b9a550f4;_tt_enable_cookie=1;_ttp=01JN21VB78XBPV6M37B8Q2ZVK7_.tt.1;_uetsid=c33bff80f78b11efac5a8f4bd6cbab70;_uetvid=78cf1120755111efa4ad5bc0b84bf60a;aws-waf-token=60a5ae66-e6d9-4f0a-baaf-d606f8bbd02c:EQoAv2ZmCpRpAQAA:bCFxDRPbtj087uUtF7xls6zba4KH2jQum614ILi9tLRCi1EVStbm+X66vCTqIg2l3TwgN1bW6+9RPtFMWr4YK1INYPqRi0XaRxQ2bXooajG1LOEUcSHKQPCMiJVHcQIdWA90B+7hpUtb4J93GSLHUFo73YtFnwkasjJcgR6Dh96jJ0vBt0J+EuRkYa/+Yd493x4bxvr9HaOxv6/DETyAjGPwG5fedNl0w9eDchmbJ8uhMcLnkbq6N06QTK8qDO8zLA==;__pdst=deedf221951f4194b4384025f3e882e8;JSESSIONID=9B8450206C4DCC9AFEFC4B7AB67ACE74;displayMode=1;sortOption=special_blend;sortOrder=1;searchMode=1;RF_BUSINESS_MARKET=21;RF_LAST_DP_SERVICE_REGION=3025;RF_LDP_VIEWS_FOR_PROMPT=%7B%22viewsData%22%3A%7B%7D%2C%22expiration%22%3A%222027-02-27T01%3A19%3A37.958Z%22%2C%22totalPromptedLdps%22%3A0%7D;RF_MARKET=north-carolina;ki_r=;ki_t=1740606838165%3B1741011664903%3B1741011664903%3B3%3B11;userPreferences=parcels%3Dtrue%26schools%3Dfalse%26mapStyle%3Ds%26statistics%3Dtrue%26agcTooltip%3Dfalse%26agentReset%3Dfalse%26ldpRegister%3Dfalse%26afCard%3D2%26schoolType%3D0%26lastSeenLdp%3DnoSharedSearchCookie%26viewedSwipeableHomeCardsDate%3D1740610826684;FEED_COUNT=%5B%22%22%2C%22t%22%5D;FEED_TIMESTAMP=1741012149764;RF_CORVAIR_LAST_VERSION=564.2.0;RF_LAST_NAV=1;RF_VISITED=true;_dd_s=isExpired=1;RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A4%2C%22events-touch%22%3Afalse%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
response = requests.request(
    "GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
'''

print(client.below_the_fold(4208613))
