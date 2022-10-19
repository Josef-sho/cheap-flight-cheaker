import requests
import datetime as dt
from pprint import pprint

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_API_KEY = "IGXLKxo5i2DacOgLsdnrcLyeCOFUAZSJ"

date = dt.datetime.now()
today = dt.datetime.now().strftime("%d/%m/%Y")
end_day = (date + dt.timedelta(days=6*30)).strftime("%d/%m/%Y")

departure_airport_code = "LON"

min_stay = 7
max_stay =28

class FlightData:
   def search_flight(self, city_name):
        self.departure_airport_code = "LON"
        self.departure_city = "LONDON"
        header = {
            "apikey": TEQUILA_API_KEY
        }
        query = {"fly_from": "LON", "fly_to": city_name,
                 "date_from": today, "date_to": end_day,
                 "nights_in_dst_from": min_stay , "nights_in_dst_to": max_stay,
                 "limit": 1, "curr": "GBP"}
        response = requests.get(url=TEQUILA_ENDPOINT, headers=header, params=query)
        self.departure_date = response.json()['data'][0]['local_departure'].split('T')[0]
        self.arrival_date = response.json()['data'][0]['utc_departure'].split('T')[0]

        return response.json()['data'][0]['price']
