# Micropython Garage Door Controller

 - [x] Simple authorization
 - [x] Access from any smartphone or PC
 - [x] Two-way communication *(every step verified)*
 - [x] Capable of controlling doors, lights and locks simultaneously
 - [ ] Live snapshots from security camera

# How does it work?

> The ESP8266 Microcontroller is connected to the Garage Door through the relay
 
> The ESP8266 communicates with the Hub through a socket on the local network

> The Hub then hosts a Telegram Bot to which authorized users may connect from their Telegram accounts



# Technology Used


**ESP8266:**
 - MicroPython 1.10
 - SRD-05VDC-SL-C relay
 
**Local Hub:**
 - Python 3
 - Telepot