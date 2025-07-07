import time
import led
import dht11 as dht_sensor
import CdS
import update_light
import soil_sensor
import write_DB as db

import os
print(os.uname())

while True:
    temp, humidity = dht_sensor.read_dht()
    if temp is not None:
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
    light_reading, light_voltage = CdS.measure_light()
    if light_reading is not None:
        print(f"Light sensor reading: {light_reading}, Voltage: {light_voltage:.2f} V")
    soil_humidity = soil_sensor.read_soil_humidity()
    if soil_humidity is not None:
        print("Soil Humidity: ", soil_humidity , "%")
    update_light.light_update(temp,humidity,light_voltage,soil_humidity)
    time.sleep(2)
    #
    fields = {
        "temperature": temp,
        "air_humidity": humidity,
        "light_reading": light_voltage,
        "soil_humidity": soil_humidity
    }

    db.send_to_influx("sensor_data", fields, tags="plant=Schefflera")
