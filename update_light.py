import check
import led

def light_update(temperature,humidity,light):
    temperature_status=check.check_threshold(temperature,"temperature")
    print(temperature_status)

    humidity_status=check.check_threshold(humidity,"humidity")
    print(humidity_status)

    light_status=check.check_threshold(light,"light")
    print(light_status)

    if temperature_status=="poor" or humidity_status=="poor" or light_status=="poor":
        led.green.off()
        led.red.on()
    else:
        led.green.on()
        led.red.off()

