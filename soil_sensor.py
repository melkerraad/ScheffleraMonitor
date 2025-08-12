from machine import ADC
import calibrations

input = ADC(26)

def read_soil_humidity():
    value = input.read_u16()  # 0 to 65535
    raw_percent = (65535 - value) / 65535 * 100  # Convert to 0-100% (wet=high, dry=low)
    
    dry = calibrations.soil_sensor_dry
    wet = calibrations.soil_sensor_wet
    
    if wet == dry:
        return 0  # no division by zero
    
    moisture_percent_calibrated = (raw_percent - dry) * 100 / (wet - dry)
    moisture_percent_calibrated = max(0, min(100, int(moisture_percent_calibrated)))
    return moisture_percent_calibrated
