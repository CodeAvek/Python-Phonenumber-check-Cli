import requests
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
import os
import pyfiglet
try :
  import phonenumbers
except ImportError:
  os.system ("pip install phonenumbers")
try:
  import pyfiglet
except ImportError:
  os.system('pip install pyfiglet')
os.system ("clear")
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

while True:
    a = input(G+'''press q to quit this code
    Enter Your PhoneNumber with +country_code :''')
    if a=="q":
        print("We SuccessFully Exited this code")
        break

    phone_number = phonenumbers.parse(a)

    print(R+"Origin country is",geocoder.description_for_number(phone_number ,"en"))

    print(R+"Company oF Sim is",carrier.name_for_number(phone_number, "en"))
