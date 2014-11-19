import pygame
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pad0 = 22
pad1 = 27
pad2 = 17
pad3 = 24
pad4 = 23

GPIO.setup(pad0, GPIO.IN)
GPIO.setup(pad1, GPIO.IN)
GPIO.setup(pad2, GPIO.IN)
GPIO.setup(pad3, GPIO.IN)
GPIO.setup(pad4, GPIO.IN)

pad0alreadyPressed = False
pad1alreadyPressed = False
pad2alreadyPressed = False
pad3alreadyPressed = False
pad4alreadyPressed = False

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

do = pygame.mixer.Sound('samples/kick.wav')
do.set_volume(.65);
re = pygame.mixer.Sound('samples/snare.wav')
re.set_volume(.65);
mi = pygame.mixer.Sound('samples/open.wav')
mi.set_volume(.65);
fa = pygame.mixer.Sound('samples/closed.wav')
fa.set_volume(.65);
sol = pygame.mixer.Sound('samples/clap.wav')
sol.set_volume(.65);

while True:
    pad0pressed = not GPIO.input(pad0)
    pad1pressed = not GPIO.input(pad1)
    pad2pressed = not GPIO.input(pad2)
    pad3pressed = not GPIO.input(pad3)
    pad4pressed = not GPIO.input(pad4)

    if pad0pressed and not pad0alreadyPressed:
        print "Pad 0 pressed"
        do.play()
    pad0alreadyPressed = pad0pressed
    print "out of if"
    print pad0pressed
    print pad0alreadyPressed

    if pad1pressed and not pad1alreadyPressed:
        print "Pad 1 pressed"
        re.play()
    pad1alreadyPressed = pad1pressed

    if pad2pressed and not pad2alreadyPressed:
        print "Pad 2 pressed"
        mi.play()
    pad2alreadyPressed = pad2pressed

    if pad3pressed and not pad3alreadyPressed:
        print "Pad 3 pressed"
        fa.play()
    pad3alreadyPressed = pad3pressed

    if pad4pressed and not pad4alreadyPressed:
        print "Pad 4 pressed"
        sol.play()
    pad4alreadyPressed = pad4pressed

    time.sleep(0.1)
