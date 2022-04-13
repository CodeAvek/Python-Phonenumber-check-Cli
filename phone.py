import os
os.system('pkg install pyhton')
os.system('pip install requests')
os.system ("pip install phonenumbers")
os.system('pip install pyfiglet')
import requests
import phonenumbers
from phonenumbers import carrier, timezone, geocoder
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
[Check Phone Number Information]
Coded By : CodeAX1
________________________________________
''')

try:
    sign = ('+')
    country_code =(input(R+'Enter Your Country Code  without + :'))
    number = (input(R+'Enter Taregt Number :'))
    a=(sign+country_code+number)
    print(Y+"Your Targeted Number is",a)

    phone_number = phonenumbers.parse(a, "GB")

    print(R+"Valid check: ",phonenumbers.is_valid_number(phone_number))
    print(R+"Company oF Sim is: ",carrier.name_for_number(phone_number, "en"))
    print(R+"Location: ",timezone.time_zones_for_number(phone_number))
    print(R+"Origin country is: ",geocoder.description_for_number(phone_number, 'en'))
    
except:   
    print('Something is wrong')
    print('Contact Owner of Script')
    
    os.system ("xdg-open https:/codeax.herokuapp.com/")
