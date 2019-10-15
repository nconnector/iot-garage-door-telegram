import time
import utime
import ubinascii
import machine
import socket
import esp
import gc

esp.osdebug(None)

client_id = ubinascii.hexlify(machine.unique_id())

pin_lights = machine.Pin(14, machine.Pin.OUT)  # pin 14/D5 for lights
pin_lights.off()
pin_door = machine.Pin(0, machine.Pin.OUT)  # pin 0/D3 for door
pin_door.off()


def door_on():
    pin_door.on()


def door_off():
    pin_door.off()


def action_door():
    pin_door.on()
    time.sleep(1)
    pin_door.off()
    print('door button pressed')


def action_lights():
    pin_lights.on()
    time.sleep(1)
    pin_lights.off()
    print('lights button pressed')


def socket_listen():
    cl, addr = sock.accept()
    print('client connected from', addr, cl)

    try:
        msg = cl.recv(1024)

        if msg == b"I'm home":
            cl.send('Going to ask Steward to open the door now.')
            action_door()
            # action_lights()
            utime.sleep(30)
            cl.send('Closing the door now.')
            action_door()
            # utime.sleep(30)
            # action_lights()
            # cl.send('Lights out.')

        elif msg == b"Click":
            cl.send('Steward will now click the button.')
            action_door()

    except Exception as e:
        cl.send(e)

    cl.close()
    gc.collect()


def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
sock = socket.socket()
sock.bind(addr)
sock.listen(1)

print('listening on', addr)

while True:
    try:
        socket_listen()
    except OSError as e:
        restart_and_reconnect()
