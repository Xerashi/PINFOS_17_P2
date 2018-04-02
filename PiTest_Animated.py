import RPi.GPIO as GPIO
import time
import pygame
import sys
from pygame.locals import *

# picture display size
width = 480
height = 320

# File names
#Happy Faces
happy1 = "/home/pi/Desktop/Animations/Wink1.png"
happy2 = "/home/pi/Desktop/Animations/Wink2,5.png"
happy3 = "/home/pi/Desktop/Animations/Wink2.png"
happy4 = "/home/pi/Desktop/Animations/Wink3.png"
#Okay Faces
okay1 = "/home/pi/Desktop/Animations/YellowBlink1.png"
okay2 = "/home/pi/Desktop/Animations/YellowBlink2.png"
okay3 = "/home/pi/Desktop/Animations/YellowBlink3.png"
#Sad Faces
sad1 = "/home/pi/Desktop/Animations/Cry1.png"
sad2 = "/home/pi/Desktop/Animations/Cry2.png"
sad3 = "/home/pi/Desktop/Animations/Cry3.png"
sad4 = "/home/pi/Desktop/Animations/Cry4.png"
#Dead faces
dead1 = "/home/pi/Desktop/Animations/Dead1.png"
dead2 = "/home/pi/Desktop/Animations/Dead2.png"
dead3 = "/home/pi/Desktop/Animations/Dead3.png"
dead4 = "/home/pi/Desktop/Animations/Dead4.png"
dead5 = "/home/pi/Desktop/Animations/Dead5.png"
dead6 = "/home/pi/Desktop/Animations/Dead6.png"
#Water animation
water1 = "/home/pi/Desktop/Animations/WaterFrame1.png"
water2 = "/home/pi/Desktop/Animations/WaterFrame2.png"
water3 = "/home/pi/Desktop/Animations/WaterFrame3.png"
water4 = "/home/pi/Desktop/Animations/WaterFrame4.png"
water5 = "/home/pi/Desktop/Animations/WaterFrame5.png"
water6 = "/home/pi/Desktop/Animations/WaterFrame6.png"
water7 = "/home/pi/Desktop/Animations/WaterFrame7.png"
water8 = "/home/pi/Desktop/Animations/WaterFrame8.png"
water9 = "/home/pi/Desktop/Animations/WaterFrame9.png"
#Startup animation
logo1 = "/home/pi/Desktop/Animations/Logo1.png"
logo2 = "/home/pi/Desktop/Animations/Logo2.png"
logo3 = "/home/pi/Desktop/Animations/Logo3.png"
logo4 = "/home/pi/Desktop/Animations/Logo4.png"
logo5 = "/home/pi/Desktop/Animations/Logo5.png"
logo6 = "/home/pi/Desktop/Animations/Logo6.png"
logo7 = "/home/pi/Desktop/Animations/Logo7.png"
logo8 = "/home/pi/Desktop/Animations/Logo8.png"

pygame.init()
windowSurfaceObj = pygame.display.set_mode((width,height),FULLSCREEN)
pygame.display.set_caption('FlowerBuddy')

#GPIO Set to PIN numbering
GPIO.setmode(GPIO.BCM)
#GPIO Killswitch
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO Water Sensor
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def WaterAnim():
	AnimationFrame(water1, 0.25)
	AnimationFrame(water2, 0.25)
	AnimationFrame(water3, 0.25)
	AnimationFrame(water5, 0.25)
	AnimationFrame(water6, 0.25)
	AnimationFrame(water7, 0.25)
	AnimationFrame(water8, 0.25)
	AnimationFrame(water9, 0.25)

def StartupAnim():
	AnimationFrame(logo1, 0.1)
	AnimationFrame(logo2, 0.1)
	AnimationFrame(logo3, 0.1)
	AnimationFrame(logo4, 0.1)
	AnimationFrame(logo5, 0.1)
	AnimationFrame(logo6, 0.1)
	AnimationFrame(logo7, 0.1)
	AnimationFrame(logo8, 2)

def HappyBlink(duration):
	AnimationFrame(happy1, duration)
	AnimationFrame(happy3, 0.5)

def OkayBlink(duration):
	AnimationFrame(okay1, duration)
	AnimationFrame(okay2, 0.5)

def SadCry(duration):
	AnimationFrame(sad1, duration)
	AnimationFrame(sad2, 0.5)
	AnimationFrame(sad3, 0.5)
	AnimationFrame(sad4, 0.5)
	AnimationFrame(sad3, 0.5)
	AnimationFrame(sad2, 0.5)

def DeadAni(duration):
	AnimationFrame(dead1, duration)
	AnimationFrame(dead2, 0.1)
	AnimationFrame(dead3, 0.1)
	AnimationFrame(dead4, 0.1)
	AnimationFrame(dead5, 0.1)
	
def LightSensor(limit):
	count = 0
	GPIO.setup(3, GPIO.OUT)
	GPIO.output(3, GPIO.LOW)
	time.sleep(0.1)
	GPIO.setup(3, GPIO.IN)
	while GPIO.input(3) == GPIO.LOW:
		count += 1
	if count >= limit:
		return 0
	if count <= limit:
		return 1

def WaterSensor():
	if GPIO.input(17) == GPIO.HIGH:
		return 1
	if GPIO.input(17) == GPIO.LOW:
		return 0



def AnimationFrame(frame, duration):
	image = pygame.image.load(frame)
	image = pygame.transform.scale(image,(width,height))
	windowSurfaceObj.blit(image,(0,0))
	pygame.display.update()
	time.sleep(duration)

def DisplayFace(f):
	if f == 1: #yes water & yes light
		image = pygame.image.load(happy1)
		image = pygame.transform.scale(image,(width,height))
	if f == 2: #yes water & no light
		image = pygame.image.load(okay1)
		image = pygame.transform.scale(image,(width,height))
	if f == 3: #no water & yes light
		image = pygame.image.load(sad1)
		image = pygame.transform.scale(image,(width,height))
	if f == 4: #no light & no water
		image = pygame.image.load(dead1)
		image = pygame.transform.scale(image,(width,height))
	windowSurfaceObj.blit(image,(0,0))
	pygame.display.update()
	time.sleep(0.01)     

