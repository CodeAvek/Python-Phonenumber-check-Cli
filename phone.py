
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

while True:
    a = input('''press q to quit this code
    Enter Your PhoneNumber with +country_code :''')
    if a=="q":
        print("We SuccessFully Exited this code")
        break

    phone_number = phonenumbers.parse(a)

    print("Origin country is",geocoder.description_for_number(phone_number ,"en"))

    print("Company oF Sim is",carrier.name_for_number(phone_number, "en"))
