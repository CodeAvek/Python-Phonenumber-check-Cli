import os
os.system('pkg install pyhton')
os.system('pkg install wget')
os.system ("pip install phonenumbers")
os.system('pip install pyfiglet')
import requests
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import os
import pyfiglet
os.system('clear')
rs = requests.session()
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
nu = 0
n = 0
br = pyfiglet.figlet_format("CodeAx1")
print(B+br)
print('''
[Check Sim Information]
Coded By : CodeAX1
________________________________________
''')
try:
    country_code =(input('Enter Your Country Code  with + sign :'))
    number = (input('Enter Taregt Number :'))
    a = (country_code+number)
    print(Y+"Your Targeted Number is",a)
    phone_number = phonenumbers.parse(a)

    print(R+"Origin country is",G+geocoder.description_for_number(phone_number ,"en"))

    print(R+"Company oF Sim is",G+carrier.name_for_number(phone_number, "en"))
    print(R+"Valid Mobile Number:",G+phonenumbers.is_valid_number(phone_number, "en"))
    print(R+"Checking possibility of Number:",G+phonenumbers.is_possible_number(phone_number, "en"))
except:
    print('Something is wrong')
    print('Contact Owner of Script')
    os.system ("xdg-open https:/codeax.herokuapp.com/")
