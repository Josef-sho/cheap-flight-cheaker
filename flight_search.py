import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "IGXLKxo5i2DacOgLsdnrcLyeCOFUAZSJ"


class FlightSearch:
    def get_destination_code(self,city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {
            "apikey": TEQUILA_API_KEY
        }
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=header, params=query)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code


