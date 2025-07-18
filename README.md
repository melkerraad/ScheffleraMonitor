# The Schefflera Monitor - by Melker Rååd (mr224tp)

The Schefflera Monitor is an IoT device suited for monitoring environmental conditions, specifically for plants. It measures temperature, air humidity, soil humidity, and lighting conditions. 
The measurements are then compared to ideal and acceptable intervals, gathered from trusted sources (see targets.py). Based on the results, a LED which is either green (ideal), yellow (acceptable)
or red (poor) will light up on the device. A poor reading also makes Grafana Unified Alerting dispatch a summary email with the latest values for all sensors and personalized recommendations to improve conditions. The hardware is relatively quick to set up, but the software aspects takes some time. A rough approximation of the total implementation time
would be 5 hours. 

# Objective

The idea for this device came from my personal lack of gardening experience. This spring, my partner has been doing an internship in another city and hence, her plants were under my care. 
However, due to my not-so-green fingers, her beloved Schefflera has started looking worse and worse. I found it difficult to cater to its needs and did not understand what I was doing wrong.
Using the Schefflera Monitor, I can utilize the power of IoT to consistently evaluate the plant's living conditions and react immediately when its condition deteriorates. Therefore, the core
objective of this project is to provide a plant monitoring system that alerts the user when a plant needs attention. Additionally, gathering data over a long period of time could provide
a good data source for a more tailored care. For instance, one could analyze fluctuations in soil and air humidity between seasons to create appropriate watering schedules. I believe that
this project will provide deep insights into plant needs and serve as a tool for learning how to take proper care of plants.

# Material

//Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.

| Component                     | Quantity | Specification                | Purpose                          |
|-------------------------------|----------|-------------------------------|----------------------------------|
| Raspberry Pi Pico WH          | 1        | RP2040 with Wi-FI and bluetooh| Microcontroller (main unit)     |
| Breadboard                    | 1        | 840 connections               | Connecting the components       |
| DHT11                         | 1        | Digital                       | Measure air humidity & temperature|
| CdS Photoresistor             | 1        | 4-7kΩ                         | Light level measurement         |
| LEDs (Red, Yellow, Green)     | 3        | 5mm, Diffuse                  | Visual feedback                 |
| 330Ω Resistors                | update   | 0.25W                         | Self-explanatory                |
| 560Ω Resistors                | update   | 0.25W                         | Self-explanatory                |
| Jumper wire cables (M/M, M/F) | Various  | 30cm                          | Circuit connections             |
| Soil Hygrometer module        | 1        | Analog + Digital output       | Measure Soil Humidity           |

I bought almost all components at [[Electrokit](https://www.electrokit.com)], all components apart from the [[Soil Hygrometer module](https://www.electrokit.com/en/jordfuktighetssensor)] and some additional [[Jumper Wire cables](https://www.amazon.se/-/en/ELEGOO-Multi-Color-Compatible-Arduino-Project/dp/B01EV70C78/ref=nav_signin?crid=1CNW654HMSUTJ&dib=eyJ2IjoiMSJ9.qTh1eH3WaOJLu45veLDAh-tkjZzYN05VXFVpEXCXp16hFg5JuWqPiWjB10J4-3bMfS44tfF6HIrWAxFPzW1KpcJIWY7siJ_pu-msBOjhW6wa08EVC0QZkcUrQEE0nnKiX9L1VHWO_d12fqbKjeYijj1x5ET4l-U-elego3Kp_QpTWUtJ2XCKjiW3zvX43lrwVB4SHA_an1ur-EyVWP-kyVZ0_cY1o32xkr43EjEnFx0IhdJBBeUGuc3yRxoVBbDepdLYaHhoCTBVrNSUAYmOs0d5a3VXLaTLVfTDDhfy2QE.gTIavKrJeXsNked39s42T2UjbokwTfyEFaY-XSeXow0&dib_tag=se&keywords=kopplingskabel&qid=1751035957&refinements=p_98%3A20692919031&rnid=20692918031&rps=1&sprefix=kopplingskabel%2Caps%2C98&sr=8-1&th=1)], was included in [[Start Kit - Applied IoT at Linnaeus University (2025)](https://www.electrokit.com/lnu-starter)]. The total cost for all components was approximately 500 SEK including shipping.

# Computer setup

When programming this device, I have been using the Visual Studio Code IDE. A crucial first step was to install the PyMAKR extension, available from the Visual Studio Code marketplace. While PyMakr [[is officially designed](https://github.com/pycom/Pymakr)] for Pycom devices, I found that it worked well for development with the Pico WH, likely since both expose a similar MicroPython USB serial interface. Using PyMAKR allowed me to upload code and interact with the device in PyMakr’s development mode. The main benefit from using the development mode is that the Pico WH is rebooted when files are changed. Hence, there was no need for manual rebooting. However since PyMakr is not officially supported for the Pico WH, some PyMAKRfeatures may be limited or unavailable. The primary script reads sensors on a one-minute interval and formats payloads in InfluxDB Line Protocol for transmission.

These were the main steps for setting up the Pico WH:
- The Pico WH was initially put into bootloader mode by holding the BOOTSEL button while connecting it to the via USB to a computer
- The latest MicroPython firmware for the Pico WH was then downloaded from the official [[Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)] and copied to the device’s USB mass storage.
- After flashing the device, it appears as a serial device over USB.
- Code is uploaded to the device and tested via PyMakr in development mode.

//How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a beginner should be able to understand.

//Chosen IDE
//How the code is uploaded
//Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.
//Putting everything together

//How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

//Circuit diagram (can be hand drawn)
//*Electrical calculations



# Platform

Platform-wise, my final setup uses InfluxDB Cloud combined with a locally hosted instance of Grafana. Initially, I experimented with a self‑hosted InfluxDB instance on a macOS server, but unfortunately I ran into a lot of networking, firewall, and binding issues that made the development and maintenance difficult. Moving to InfluxDB Cloud eliminated many of these issues, and it was very easy to use as a data source in Grafana. 

InfluxDB Cloud offers [[multiple subscription types](https://www.influxdata.com/influxdb-pricing/?_gl=1*15yxm1o*_gcl_au*MTAzOTcxMzUwNy4xNzUxNjU3MTMz*_ga*MTE2MTYyMDY0OS4xNzUxNjU3MTMz*_ga_CNWQ54SDD8*czE3NTE4NDY4NTEkbzUkZzEkdDE3NTE4NDY4NjkkajQyJGwwJGg0OTExMzExMA..)], and I decided to go for the free version. This version includes 30 days data storage, alerts (only on Slack) and up to 1,000 kb/s reads and 17 kb/s writes for up to 10,000 series. If you remember, this project enables alerts by email as well. However, the alerts are setup from the Grafana instance and not the InfluxDB cloud, hence being limited to Slack by InfluxDB does not affect the project. If this project's scope was extended, one would likely want to investigate the other subscription options. The main benefit of upgrading to a paid plan would be a data retention exceeding 30 days. Additionally, as all alert handlers (including email) are available for paid subscriptions, the alert responsibility could be moved from Grafana to InfluxDB. Hence, the project could be made less dependent on Grafana and only use it for visualization purposes. 




---continue---
Describe platform in terms of functionality
*Explain and elaborate what made you choose this platform

#The code

Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.

import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Transmitting the data / connectivity

Every minute the Pico WH sends a payload such as:
```python
sensor_data temperature=23,air_humidity=45,light_reading=12000,soil_humidity=36
```


How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

How often is the data sent?
Which wireless protocols did you use (WiFi, LoRa, etc …)?
Which transport protocols were used (MQTT, webhook, etc …)
*Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.

# Presenting the data

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

Provide visual examples on how the dashboard looks. Pictures needed.
How often is data saved in the database.
*Explain your choice of database.
*Automation/triggers of the data.

# Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

Show final results of the project
Pictures
*Video presentation
