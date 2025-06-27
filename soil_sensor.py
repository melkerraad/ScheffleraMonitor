from machine import ADC

input = ADC(26)

def read_soil_humidity():
    value = input.read_u16() # The sensor presents a 16-bit value from 0 to 65535
    moisture_percent = (65535 - value) / 65535 * 100  # convert 16-bit value to percentage
    return moisture_percent