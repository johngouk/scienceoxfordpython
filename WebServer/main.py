"""

    Demo asyncio Web Server for SciOx Python in Education
    

"""

import time, random, logging
from micropython import const
import asyncio
import random
import os, gc
from machine import Pin

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)
# JDG Mod to get (msecs) logging keyword to work
try:
    from ESPLogRecord import ESPLogRecord
    logger.record = ESPLogRecord()
except ImportError:
    pass

from RequestParser import RequestParser
from ResponseBuilder import ResponseBuilder
from WiFiConnection import WiFiConnection
from flashLed import flashLed
from WebServer import WebServer

"""
************************************************

    main
    - starts all the different coroutines
    - Continuously runs to maintain everything
    - flashes the LED on the board every 1 sec to show it's working

************************************************
"""
async def main():

    # start web server task
    ws.run()
    
    # main task control loop pulses board led
    while True:
        # Read the notes about memory at
        # https://docs.micropython.org/en/latest/reference/speed_python.html#controlling-gc
        gc.collect() # Particularly important on the ESP8266 lil' guy
        flashLed.toggle_red_led() # Tell people we're doing something
        await asyncio.sleep(1)


"""
************************************************

    Programme starts here
    Order of commands is important, because you can't call an object
    that hasn't been initialised
    So:
    1 - WiFi otherwise nothing happens
    2 - Web server, which calls the other objects for data
    3 - The main loop

************************************************
"""

logger.info("Program starting")

# 1
ok = WiFiConnection.start_station_mode()
if ok:
    # Set up as STA
    pass
else:
    logger.warning("WiFi STA mode failed, cause %s : trying AP mode", WiFiConnection.statusText)
    password = 'password'
    if WiFiConnection.start_ap_mode(ssid="", password=password):
        logger.info("WiFi AP mode started as network SSID %s Pwd: %s Server IP: %s", WiFiConnection.ap_ssid, password, WiFiConnection.ap_ip)
    else:
        raise RuntimeError('Unable to connect to network or start AP mode')

# 2
# My WebServer class can interrogate other objects for data, but we aren't using
# that feature in this demo
# ws = WebServer(dataSources=[list of methods to call for data], docroot="directory for web docs")
ws = WebServer()

# 3
try:
    # start the main async tasks
    asyncio.run(main())
finally:
    # reset and start a new event loop for the task scheduler
    asyncio.new_event_loop()
