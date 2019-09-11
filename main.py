#!/usr/bin/env python3
import blynklib
from display_mod import *
import random
ORDER = neopixel.GRBW
num_pix = 17

crickit.init_neopixel(num_pix, bpp=4, pixel_order=ORDER)
np = crickit.neopixel

BLYNK_AUTH = 'ajq967lHRoPNlPZZObQ_mcWo2N8XyTHc'
blynk = blynklib.Blynk(BLYNK_AUTH, server='192.168.1.141', port=8080)

@blynk.handle_event('write V0')
def animate_pix1(pin, value):
    if int(value[0]) == 1:
        fill_strip(np, num_pix, AQUA)
        sleep(0.1)
    if int(value[0]) == 0:
        fill_strip(np, num_pix, BLACK)
        sleep(0.1)

@blynk.handle_event('write V1')
def animate_pix2(pin, value):
    if int(value[0]) == 1:
        randomFlashes(np, 4)
        sleep(0.1)

@blynk.handle_event('write V2')
def animate_pix3(pin, value):
    if int(value[0]) == 1:
        fill_strip(np, num_pix, randColor())
        sleep(0.1)
    if int(value[0]) == 0:
        fill_strip(np, num_pix, BLACK)
        sleep(0.1)

@blynk.handle_event('write V3')
def animate_pix4(pin, value):
    if int(value[0]) == 1:
        randFill(np, num_pix)
        sleep(0.1)
    if int(value[0]) == 0:
        fill_strip(np, num_pix, BLACK)
        sleep(0.1)

@blynk.handle_event('write V4')
def animate_pix(pin, value):
    if int(value[0]) == 1:
        COL = randColor()
        runner(np, num_pix, COL)
    if int(value[0]) == 0:
        runner(np, num_pix, BLACK)

@blynk.handle_event('write V5')
def kill_strip(pin, value):
    if int(value[0]) == 1:
        np.fill(BLACK)
        np.fill(BLACK)



while True:
    blynk.run()
