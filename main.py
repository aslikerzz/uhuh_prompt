import os
import time
import subprocess
import colorama
from colorama import Fore, Style, init

init()

def clear():
    os.system("cls" if os.name == 'nt' else "clear")

def help():
    print("""             
          
                ----------[ HELP MENU ]----------
                    
                help : access help menu
                args: -u : uhuh help
                      -n : network help
                
                n : network menu
                args: -h : network help
                      -on : enable network tool
                      -off : disable network tool
                      -a : add the address to scan/work on (read man on -h)
                      -nw : shows all wlans profiles
                      
                uhuh : as a prefix (read man on -u)
                
                """)


# network tools

def nw():
    print(Fore.LIGHTCYAN_EX)
    print(os.system('netsh wlan show profiles'))




while True:
    user_input = input(Fore.LIGHTGREEN_EX + "uhuh@user+: " + Fore.LIGHTBLUE_EX)
    if user_input == 'bye':
        break
    elif user_input == 'help':
        help()
    elif user_input == 'help -u':
        print(Fore.WHITE + """help uhuh :
              it's useful i swear""" + Fore.RESET)
    elif user_input == 'help -n':
        print(Fore.WHITE + """help network :
              soon""" + Fore.RESET)
    elif user_input == 'n':
        print(Fore.YELLOW + """network tool, here's what u can do when using it :
              administration, organisation, more soon""" + Fore.RESET)
    elif user_input == 'n -on':
        print(Fore.WHITE + "network tool => [" + Fore.GREEN + "on" + Fore.WHITE + "]" + Fore.RESET)
    elif user_input == 'n -off':
        print(Fore.WHITE + "network tool => [" + Fore.RED + "off" + Fore.WHITE + "]" + Fore.RESET)
    elif user_input == 'n -a':
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[SOON]" + Fore.RESET + Style.RESET_ALL)
    elif user_input == 'n -h':
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "[SOON]" + Fore.RESET + Style.RESET_ALL)
    elif user_input == 'cls':
        clear()
    elif user_input == 'n -nw':
        nw()
        