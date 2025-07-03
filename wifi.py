import network
import time

def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        status = wlan.status()
        print("Status:", status)  #debug print
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        time.sleep(1)

    if wlan.status() != 3:
        print('Failed to connect to Wi-Fi')
    else:
        status = wlan.ifconfig()
        print(f"IP address:{status[0]}")
        return status[0]
