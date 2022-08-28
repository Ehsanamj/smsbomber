import requests
from time import sleep
from colorama import Fore as color  
import json
import random
from datetime import datetime
def gapfilm(number):
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
    info = {"Type":3,"Username":number,"SourceChannel":"GF_WebSite","SourcePlatform":"desktop","SourcePlatformAgentType":"Firefox","SourcePlatformVersion":"99.0",}
    gapfilm = 'https://core.gapfilm.ir/api/v3.1/Account/Login'

    
    try:
        req = requests.post(gapfilm, data=info, headers=rhead)
        print(req.status_code)
        sleep(0.5)
        try:
            print(color.GREEN+"[*] gapfilm Sent...!",end= '')
            time = datetime.now()
            print(color.LIGHTGREEN_EX+ bold +'\t'+str(time.hour)+":"+str(time.minute)+":"+str(time.second))
        except:
            print(color.RED+"[-] Something Went Wrong...") 
            raise        
    except:
        print("something went wrong...")
        raise



#url =('https://core.gapfilm.ir/api/v3.1/Account/Login')
#data = {"Type":3,"Username":phonenum,"SourceChannel":"GF_WebSite","SourcePlatform":"desktop","SourcePlatformAgentType":"Firefox","SourcePlatformVersion":"99.0",}
