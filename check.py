import target

def check_threshold(measurement, type):
    if type == "temperature":
        if target.ideal_temperature[0] <= measurement <= target.ideal_temperature[1]:
            return "ideal"
        elif target.acceptable_temperature[0] <= measurement <= target.acceptable_temperature[1]:
            return "acceptable"
        else:
            return "poor"

    if type == "humidity":
        if target.ideal_humidity[0] <= measurement <= target.ideal_humidity[1]:
            return "ideal"
        elif target.acceptable_humidity[0] <= measurement <= target.acceptable_humidity[1]:
            return "acceptable"
        else:
            return "poor"
