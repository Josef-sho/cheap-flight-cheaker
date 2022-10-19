import requests
sheety_api = "https://api.sheety.co/9595023b8abf54e7f2e3aeb0091976ec/newFlightDeals/prices"



class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_destination_data(self):

        response = requests.get(url=sheety_api)

        self.sheet_data = [response.json()["prices"]]
        return self.sheet_data

    def update_destination_codes(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_api}/{city['id']}",
                json=new_data,
            )
            print(response.text)
            print(self.sheet_data)
