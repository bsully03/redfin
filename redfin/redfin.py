
import json
import requests
import browser_cookie3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Redfin:
    def __init__(self):
        self.base = 'https://www.redfin.com/stingray/'
        
        self.headers = {
            'cookie': self.load_chrome_cookies(False, 'redfin.com'),
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        
    def load_chrome_cookies(self, force, domain):
        """Loads Chrome cookies for a specific domain."""
        if force:
            cookies = self.get_chrome_cookies_exact(domain)
            cookie = [f'{c["name"]}={c['value']}' for c in cookies]
        else:
            # Look for cookies.txt file in root
            try:
                with open('cookies.txt', 'r') as f:
                    return f.read()
            except FileNotFoundError:
                cj = browser_cookie3.chrome()
                cj = [c for c in cj if c.domain.endswith(domain)]
                cookie = [f'{cookie.name}={cookie.value}' for cookie in cj if cookie.domain.endswith(domain)]
        
        cooks = ';'.join(cookie)
        with open('cookies.txt', 'w') as f:
            f.write(cooks)
        
        return cooks


    def get_chrome_cookies_exact(self, url: str):
        """
        Returns ALL cookies visible in Chrome DevTools for the given URL.
        Uses Chrome DevTools Protocol (CDP): Network.getCookies.
        """
        # --- Launch Chrome with CDP ---
        chrome_options = Options()
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)

        # --- Load the page (important: Chrome will populate cookies for its TLD) ---
        if not url.startswith('https://www.'):
            url = 'https://www.' + url
        
        driver.get(url)

        # --- Fetch cookies via CDP (this is what DevTools uses) ---
        raw = driver.execute_cdp_cmd("Network.getCookies", {})

        cookies = raw.get("cookies", [])

        driver.quit()
        return cookies

    def meta_property(self, url, kwargs, page=False):
        if page:
            kwargs['pageType'] = "3"
        return self.meta_request('api/home/details/' + url, {
            'accessLevel': "1",
            **kwargs
        })
        

    def meta_request(self, url, kwargs):
        try:
            response = requests.request("GET",
                self.base + url, data = '', params=kwargs, headers=self.headers)
            response.raise_for_status()
            return json.loads(response.text[4:])
        except:
            headers = self.load_chrome_cookies(True, 'redfin.com')
            response = requests.request("GET",
                self.base + url, data='', params=kwargs, headers=headers)
            response.raise_for_status()
            return json.loads(response.text[4:])

    # Url Requests

    def initial_info(self, url, **kwargs):
        return self.meta_request('api/home/details/initialInfo', {'path': url, **kwargs})

    def page_tags(self, url, **kwargs):
        return self.meta_request('api/home/details/v1/pagetagsinfo', {'path': url, **kwargs})

    def primary_region(self, url, **kwargs):
        return self.meta_request('api/home/details/primaryRegionInfo', {'path': url, **kwargs})

    # Search
    def search(self, query, **kwargs):
        return self.meta_request('do/location-autocomplete', {'location': query, 'v': 2, **kwargs})

    # Property ID Requests
    def below_the_fold(self, property_id, **kwargs):
        return self.meta_property('belowTheFold', {'propertyId': f"{property_id}", **kwargs}, page=True)

    def hood_photos(self, property_id, **kwargs):
        return self.meta_request('api/home/details/hood-photos', {'propertyId': property_id, **kwargs})

    def more_resources(self, property_id, **kwargs):
        return self.meta_request('api/home/details/moreResourcesInfo', {'propertyId': property_id, **kwargs})

    def page_header(self, property_id, **kwargs):
        return self.meta_request('api/home/details/homeDetailsPageHeaderInfo', {'propertyId': property_id, **kwargs})

    def property_comments(self, property_id, **kwargs):
        return self.meta_request('api/v1/home/details/propertyCommentsInfo', {'propertyId': property_id, **kwargs})

    def building_details_page(self, property_id, **kwargs):
        return self.meta_request('api/building/details-page/v1', {'propertyId': property_id, **kwargs})

    def owner_estimate(self, property_id, **kwargs):
        return self.meta_request('api/home/details/owner-estimate', {'propertyId': property_id, **kwargs})

    def claimed_home_seller_data(self, property_id, **kwargs):
        return self.meta_request('api/home/details/claimedHomeSellerData', {'propertyId': property_id, **kwargs})

    def cost_of_home_ownership(self, property_id, **kwargs):
        return self.meta_request('do/api/costOfHomeOwnershipDetails', {'propertyId': property_id, **kwargs})

    # Listing ID Requests
    def floor_plans(self, listing_id, **kwargs):
        return self.meta_request('api/home/details/listing/floorplans', {'listingId': listing_id, **kwargs})

    def tour_list_date_picker(self, listing_id, **kwargs):
        return self.meta_request('do/tourlist/getDatePickerData', {'listingId': listing_id, **kwargs})

    # Table ID Requests

    def shared_region(self, table_id, **kwargs):
        return self.meta_request('api/region/shared-region-info', {'tableId': table_id, 'regionTypeId': 2, 'mapPageTypeId': 1, **kwargs})

    # Property Requests

    def similar_listings(self, property_id, listing_id, **kwargs):
        return self.meta_property('similars/listings', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def similar_sold(self, property_id, listing_id, **kwargs):
        return self.meta_property('similars/solds', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def nearby_homes(self, property_id, listing_id, **kwargs):
        return self.meta_property('nearbyhomes', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def above_the_fold(self, property_id, listing_id, **kwargs):
        return self.meta_property('aboveTheFold', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def property_parcel(self, property_id, listing_id, **kwargs):
        return self.meta_property('propertyParcelInfo', {'propertyId': property_id, 'listingId': listing_id, **kwargs}, page=True)

    def activity(self, property_id, listing_id, **kwargs):
        return self.meta_property('activityInfo', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def customer_conversion_info_off_market(self, property_id, listing_id, **kwargs):
        return self.meta_property('customerConversionInfo/offMarket', {'propertyId': property_id, 'listingId': listing_id, **kwargs}, page=True)

    def rental_estimate(self, property_id, listing_id, **kwargs):
        return self.meta_property('rental-estimate', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def avm_historical(self, property_id, listing_id, **kwargs):
        return self.meta_property('avmHistoricalData', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def info_panel(self, property_id, listing_id, **kwargs):
        return self.meta_property('mainHouseInfoPanelInfo', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def descriptive_paragraph(self, property_id, listing_id, **kwargs):
        return self.meta_property('descriptiveParagraph', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def avm_details(self, property_id, listing_id, **kwargs):
        return self.meta_property('avm', {'propertyId': property_id, 'listingId': listing_id, **kwargs})

    def tour_insights(self, property_id, listing_id, **kwargs):
        return self.meta_property('tourInsights', {'propertyId': property_id, 'listingId': listing_id, **kwargs}, page=True)

    def stats(self, property_id, listing_id, region_id, **kwargs):
        return self.meta_property('stats', {'regionId': region_id, 'propertyId': property_id, 'listingId': listing_id, 'regionTypeId': 2, **kwargs})
