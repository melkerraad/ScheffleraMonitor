from machine import ADC, Pin
import time

#CdS is connected to an ADC on GP27
CdS = ADC(27)

def measure_light():
    reading = CdS.read_u16()  # The sensor presents a 16-bit value from 0 to 65535
    voltage = reading * 3.3 / 65535    # Converting the reading to voltage
    return reading,voltage
