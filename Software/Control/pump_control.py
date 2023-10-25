# Pump control
#imports
import RPi.GPIO as GPIO
import time
import cv2
import keyboard

#define pins
enable_pin = 33
in1_pin = 35
in2_pin = 36

def conf():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(enable_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(in1_pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(in2_pin, GPIO.OUT, initial=GPIO.LOW)

def start():
    GPIO.output(enable_pin, GPIO.HIGH)

def stop():
    GPIO.output(enable_pin, GPIO.LOW)
    GPIO.output(in1_pin, GPIO.LOW)
    GPIO.output(in2_pin, GPIO.LOW)


def forward():
    start()
    GPIO.output(in1_pin, GPIO.HIGH)
    GPIO.output(in2_pin, GPIO.LOW)

def reverse():
    start()
    GPIO.output(in1_pin, GPIO.LOW)
    GPIO.output(in2_pin, GPIO.HIGH)

def pumpControl():
    conf()
    while True:
        keyCode = cv2.waitKey(10) & 0xFF
        if keyboard.is_pressed('q') or keyCode == 27:
            stop()
            print("closing...")
            break
        elif keyboard.is_pressed('f'):
            print("forward...")
            start()
            forward()
            time.sleep(15)
            stop()
            print("Complete.")
        elif keyboard.is_pressed('r'):
            print("reverse...")
            start()
            reverse()
            time.sleep(15)
            stop()
            print("Complete.")
        elif keyboard.is_pressed('x'):
            print("disabled...")
            stop()





















