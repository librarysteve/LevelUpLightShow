#!/usr/bin/env python3
import requests
import os
from time import sleep

server = 'http://0.0.0.0:8080/'
api_key = ('KEY_PI_1', 'KEY_PI_2', 'KEY_PI3_3', 'KEY_PI_4')
mode = '/update/'


##print(server + api_key[2] + mode + 'V0?value=1' )

def out_funk():
    os.system("clear")
    os.system("cowsay Cleaning Up! | lolcat")
    for i in range(len(api_key)):
        call(api_key[i],  'V5')

def call(key, pin):
    send_on = (server + key + mode + str(pin) + '?value=' + str(1))
    print("Calling: \n")
    print(send_on)
    requests.get(send_on)
    sleep(0.7)
    send_off = (server + key + mode + str(pin) + '?value=' + str(0))
#    print("Calling: \n")
#    print(send_off)
    requests.get(send_off)
    sleep(0.7)

def make_the_calls():
    call(api_key[0], 'V0')
    call(api_key[1], 'V0')
    call(api_key[2], 'V0')
    sleep(1)
    call(api_key[0], 'V1')
    call(api_key[1], 'V1')
    call(api_key[2], 'V1')
    sleep(1)
    call(api_key[0], 'V2')
    call(api_key[1], 'V2')
    call(api_key[2], 'V2')
    sleep(1)
    call(api_key[0], 'V3')
    call(api_key[1], 'V3')
    call(api_key[2], 'V3')
    sleep(1)
    call(api_key[0], 'V4')
    call(api_key[1], 'V4')
    call(api_key[2], 'V4')
## MAIN FUNK ##
make_the_calls()

## CLEAN UP ##
out_funk()
