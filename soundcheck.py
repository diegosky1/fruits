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

    do.play()
    time.sleep(1)
    re.play()
    time.sleep(1)
    mi.play()
    time.sleep(1)
    fa.play()
    time.sleep(1)
    sol.play()
    time.sleep(1)
    do.play()
    time.sleep(1)
