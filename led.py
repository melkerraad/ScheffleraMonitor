from machine import Pin
import time

red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

def blink(led, duration=1):
    led.on()
    time.sleep(duration)
    led.off()
    time.sleep(duration)