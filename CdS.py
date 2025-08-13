from machine import ADC, Pin
import time
import calibrations

#CdS is connected to an ADC on GP27
CdS = ADC(27)

def measure_light():
    reading = CdS.read_u16()  # The sensor presents a 16-bit value from 0 to 65535
    voltage = reading * 3.3 / 65535    # Converting the reading to voltage

    dark_raw = calibrations.light_sensor_darkness
    sun_raw = calibrations.light_sensor_sun

    if sun_raw == dark_raw:
        calibrated_voltage = 0.0
    else:
        normalized = (reading - dark_raw) / (sun_raw - dark_raw)
        normalized = max(0, min(1, normalized))
        calibrated_voltage = normalized * 3.3  # i scale it to voltage range

    return reading, calibrated_voltage
