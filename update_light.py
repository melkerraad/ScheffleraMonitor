import check
import led

def light_update(temperature,humidity,light,soil_humidity):
    temperature_status=check.check_threshold(temperature,"temperature")
    
    air_humidity_status=check.check_threshold(humidity,"humidity")

    light_status=check.check_threshold(light,"light")
    
    soil_humidity_status=check.check_threshold(soil_humidity,"soil_humidity")

    if temperature_status=="poor" or air_humidity_status=="poor" or light_status=="poor" or soil_humidity_status=="poor":
        led.green.off()
        led.yellow.off()
        led.red.on()

    elif temperature_status=="acceptable" or air_humidity_status=="acceptable" or light_status=="acceptable" or soil_humidity_status=="acceptable":
        led.green.off()
        led.red.off()
        led.yellow.on()
        
    else:
        led.green.on()
        led.red.off()
        led.yellow.off()

#