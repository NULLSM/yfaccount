import requests
import json
import datetime 
import random 
import string 
import time 
import os 
import sys
import urllib.parse
 
from requests.structures import CaseInsensitiveDict

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	

url = "https://www.your-freedom.net/api.php"

headers = CaseInsensitiveDict()
headers["Content-Length"] = "177"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Host"] = "www.your-freedom.net"
headers["Connection"] = "Keep-Alive"
username=genString(10)
password=digitString(16)

da = {
  "cmd":"create_account",
  "data":{
    "username":username,
    "password":password,
    "email":genString(16)+"@gmail.com",
    "no_verification":True}
}



dat =urllib.parse.urlencode(da)
d1 = dat.replace('%27','%22')
d2 = d1.replace('+','')


data=d2

resp = requests.post(url, headers=headers, data=data)

print(resp.text)
print("\nUsername : "+username)
print("\nPassword : "+password)


