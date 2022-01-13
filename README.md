# Python-Phonenumber-check-Cli
In This Code We Will Execute from the Given Number The Origin Of Sim country And The Company Belongs To Like Jio,Airtel,Vodephone Etc
# First Of All Open Your Terminal And Install Your Module : pip install phonenumers
# After Successfully installation of module you have to open your file and code are given below
# Written by CodeAx
# Write the +91 in the begining of phone number::::While using

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
