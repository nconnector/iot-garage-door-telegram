
"""
 - kill AP
 - connect to WiFi
"""


def do_connect():
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('SSID', 'PSK')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
