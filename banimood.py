import requests
from time import sleep
from colorama import Fore as color  
import json
import random
from datetime import datetime
def bani(number):
    bold ='\033[1m'

    heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
    
    rhead = random.choice(heads)
    info = {"phone":number}
    ketabaz = 'https://mobapi.banimode.com/api/v2/auth/request'

    
    try:
        req = requests.post(ketabaz, data=info, headers=rhead)
        print(req.status_code)
        sleep(0.5)
        try:
            print(color.GREEN+"[*] banimood Sent...!",end= '')
            time = datetime.now()
            print(color.LIGHTGREEN_EX+ bold +'\t'+str(time.hour)+":"+str(time.minute)+":"+str(time.second))
        except:
            print(color.RED+"[-] Something Went Wrong...") 
            raise        
    except:
        print("something went wrong...")
        raise

#url =('https://mobapi.banimode.com/api/v2/auth/request')
#data= {"phone":phonenum}
