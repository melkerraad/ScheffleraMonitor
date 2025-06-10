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
        led.yellow.off()
        led.red.on()

    elif temperature_status=="acceptable" or humidity_status=="acceptable" or light_status=="acceptable":
        led.green.off()
        led.red.off()
        led.yellow.on()
    else:
        led.green.on()
        led.yellow.off()
        led.red.off()

