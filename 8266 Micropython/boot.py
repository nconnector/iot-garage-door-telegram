
# This file is executed on every boot (including wake-boot from deepsleep)

# import esp

# esp.osdebug(None)

import uos, machine

# uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

from wifi import do_connect

# import webrepl

# webrepl.start()
do_connect()

gc.collect()







