from machine import Pin
import time
import led
import dht_sensor

while True:
    led.blink(led.red)
    led.blink(led.yellow)
    led.blink(led.green)
    temp, humidity = dht_sensor.read_dht()
    if temp is not None:
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
    time.sleep(2)