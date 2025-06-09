from machine import Pin
import time

led_red = Pin(15, Pin.OUT)
led_yellow = Pin(14, Pin.OUT)
led_green = Pin(13, Pin.OUT)

while True:
    led_red.on()
    time.sleep(1)
    led_red.off()
    time.sleep(1)
    led_yellow.on()
    time.sleep(1)
    led_yellow.off()
    time.sleep(1)
    led_green.on()
    time.sleep(1)
    led_green.off()
    time.sleep(1)