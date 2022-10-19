import requests

sheety_api = "https://api.sheety.co/9595023b8abf54e7f2e3aeb0091976ec/newFlightDeals/users"

first_name = input("What is your first name")
last_name = input("what is your last name")

email = None
confirm_email = None


def ask_email():
    global email, confirm_email
    email = input("what is your email")
    confirm_email = input("confirm email")


ask_email()
if email == confirm_email:
    new_data = {'users': {
        "First Name": first_name,
        "Last Name": last_name,
        "Email": confirm_email
    }}
    response = requests.post(url=sheety_api,
                             json=new_data)

    print("you are in the flight club")
