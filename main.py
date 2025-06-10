from machine import Pin
import time
import led
import dht11 as dht_sensor
import CdS
import isIdeal

while True:
    led.blink(led.red)
    led.blink(led.yellow)
    led.blink(led.green)
    temp, humidity = dht_sensor.read_dht()
    if temp is not None:
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
    light_reading, light_voltage = CdS.measure_light()
    if light_reading is not None:
        print(f"Light sensor reading: {light_reading}, Voltage: {light_voltage:.2f} V")
    time.sleep(2)

    if isIdeal(humidity,"humidity"):
        print("humidity ideal")
    