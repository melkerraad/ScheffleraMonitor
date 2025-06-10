from machine import Pin
import dht
import time

dht11 = dht.DHT11(Pin(17))

def read_dht():
    try:
        dht11.measure()
        temp = dht11.temperature()
        humidity = dht11.humidity()
        return temp, humidity
    except OSError as e:
        print("Failed to read from DHT11:", e)
        return None, None
