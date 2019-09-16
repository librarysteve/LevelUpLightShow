#!/usr/bin/env python3
import blynklib
from time import sleep
import os
import requests
from get_combo import getCombo
from colorama import colorama_text, Fore

BLYNK_AUTH = 'API_FOR_ANDROID_APP'
blynk = blynklib.Blynk(BLYNK_AUTH, server='0.0.0.0', port='8080')

def wrong_combo():
    os.system("clear")
    with colorama_text():
        print(Fore.LIGHTRED_EX)
        os.system("cowsay you have...")
        os.system("figlet FAILED!")
        sleep(0.5)
        os.system("clear")
        sleep(0.5)
        os.system("cowsay you have...")
        os.system("figlet FAILED!")
        sleep(0.5)
        os.system("clear")
        sleep(0.5)
        os.system("cowsay you have...")
        os.system("figlet FAILED!")
        sleep(1)
        os.system("clear")
        print(Fore.LIGHTMAGENTA_EX)
        os.system("figlet TRY AGAIN?")
        print(Fore.RESET)


def right_combo():
    os.system("clear")
    os.system("cowsay MOOOOOOOOOOO... | lolcat")
    os.system("figlet SUCCESS! | lolcat")
    sleep(0.75)
    os.system("clear")
    os.system("cowsay You should... | lolcat")
    sleep(0.75)
    os.system("echo LOOK UP! '\ue286' | figlet | lolcat")
    sleep(3)
    reset_term()

def reset_term():
    os.system("clear")
    with colorama_text():
        print(Fore.LIGHTMAGENTA_EX)
        os.system("figlet Enter Code!")
        print(Fore.RESET)


@blynk.handle_event('write V0')
def run_script(pin, value):
    if int(value[0]) == 1:
        current_combo = getCombo()
        if current_combo == '["1"]["2"]["3"]["4"]':
           right_combo()

        else:
            wrong_combo()

@blynk.handle_event('write V5')
def reset_button(pin, value):
    if (int(value[0])) == 1:
        reset_term()


while True:
    blynk.run()
