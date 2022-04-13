
# Python-Phonenumber-check-Cli


## CodeAx

 - [Telegram](https://t.me/avekgaming)
 - [instagram](https://instagram.com/codeax1?utm_medium=copy_link)
 - [Youtube](https://youtube.com/channel/UC-Q6ZcOtcx1gZ9fI5MDDt3w)


## important to check

- First Of All Open Your Terminal And Install Your Module : pip install phonenumers
- After Successfully installation of module you have to open your file and code are given below
- Written by CodeAx
-  Write the +91 in the begining of phone number::::While using


## Deployment

open your python script and write your code

```bash
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


```

## Run On Termux

```
apt update && apt upgrade
```

```
wget https://raw.githubusercontent.com/CodeAvek/Python-Phonenumber-check-Cli/main/phone.py
```

```
ls
```

```
python phone.py
```
