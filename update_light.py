import check
import led

def light_update(temperature,humidity,light):
    temperature_status=check.check_threshold(temperature,"temperature")
    
    humidity_status=check.check_threshold(humidity,"humidity")

    light_status=check.check_threshold(light,"light")

    if temperature_status=="poor" or humidity_status=="poor" or light_status=="poor":
        led.green.off()
        led.red.on()
    else:
        led.green.on()
        led.red.off()

