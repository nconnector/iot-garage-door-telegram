
## Micropython Garage Door Controller

<img src="https://github.com/nconnector/iot-garage-door-telegram/raw/master/screenshot.png" width=40% img align="right">

 - [x] Simple authorization
 - [x] Access from any smartphone or PC
 - [x] Two-way communication *(every step verified)*
 - [x] Capable of controlling doors, lights and locks simultaneously
 - [ ] Live snapshots from security camera

### How does it work?

The ESP8266 Microcontroller is connected to the Garage Door through the relay
 
The ESP8266 communicates with the Hub through a socket on the local network

The Hub then hosts a Telegram Bot to which authorized users may connect from their Telegram accounts

## Prerequisites

- Wired garage door

- ESP8266, ESP32 or another microcontroller

- A 3V or 5V relay (depending on your controller)

- Local hub with Python 3.6+ (windows, linux, rasbpian, etc...) 

## Installation

This version is set up for a Windows local hub, but it will take little change to adapt it for Unix.

1. Burn the firmware from this repo or [from here](https://micropython.org/download) onto your controller

2. Upload scripts from [8266 Micropython](https://github.com/nconnector/iot-garage-door-telegram/tree/master/8266%20Micropython "8266 Micropython") folder to the controller

3. Add your SSID and PSK to wifi.py on the controller

4. Rename config_example.ini to config.ini

5. Set up a telegram bot, note your bot's API key and Telegram user id

6. Populate config.ini with the API key and your user id as admin, as well as trusted users that will not have to register through the bot

7. In the config, set ESP8266_IP to your controller's local IP address

8. Power up the controller and run telegram.py

## Technology Used


**ESP8266:**
 - MicroPython 1.10
 - SRD-05VDC-SL-C relay
 
**Local Hub:**
 - Python 3
 - Telepot