import time
import led
import dht11 as dht_sensor
import CdS
import update_light

while True:
    temp, humidity = dht_sensor.read_dht()
    if temp is not None:
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
    light_reading, light_voltage = CdS.measure_light()
    if light_reading is not None:
        print(f"Light sensor reading: {light_reading}, Voltage: {light_voltage:.2f} V")
    update_light.light_update(temp,humidity)
    time.sleep(2)
#