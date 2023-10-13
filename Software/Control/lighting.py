# Lighting control
#imports
import RPi.GPIO as GPIO
import time
import cv2
import keyboard

#define pins
enable_pin = 12

def conf():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(enable_pin, GPIO.OUT, initial=GPIO.LOW)

def light_on():
    conf()
    GPIO.output(enable_pin, GPIO.HIGH)

def light_off():
    conf()
    GPIO.output(enable_pin, GPIO.LOW)