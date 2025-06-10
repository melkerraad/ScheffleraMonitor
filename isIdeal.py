import ideal_values

def isIdeal(measurement, type):
    if type=="humidity":
        if measurement in ideal_humidity:
            return True
