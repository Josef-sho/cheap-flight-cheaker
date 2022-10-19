import smtplib
my_email = "josefsho90@gmail.com"
password = "oxjwqyefxndqbbuf"


from data_manager import DataManager
from flight_data import FlightData

data_sheet = DataManager()
data = data_sheet.get_destination_data()[0]

flight_search = FlightData()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


if data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight = FlightSearch()
    for row in data:
        row['iataCode'] = flight.get_destination_code(row["city"])
    print(f"sheet_data:\n {data}")

    data_sheet.sheet_data = data
    data_sheet.update_destination_codes()


for row in data:
    code = row['iataCode']
    price = flight_search.search_flight(code)
    city = row['city']
    print(f"{city}   €{price}")
    if price <= row['lowestPrice']:
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="josephshodunke4@gmail.com",
                                msg=f"Subject:low price\n\nLow price Alert only €{price} to fly from "
                                    f"{flight_search.departure_city}-{flight_search.departure_airport_code} to {city}-{code}"
                                    f" form {flight_search.departure_date} to {flight_search.arrival_date}")

