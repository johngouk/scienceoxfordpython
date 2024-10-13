"""

    asyncio demo - should work on CPython and MicroPython, right??

"""
import time
import asyncio
import logging

MP = False

# micropython
import sys
if sys.implementation.name == "micropython":
    MP = True
    from micropython import const
    import network
    import ntptime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)
if MP:
    from ESPLogRecord import ESPLogRecord
    logger.record = ESPLogRecord()

#from WiFiConnection import WiFiConnection

async def doSomething(interval, name):
    # Prints the message as a logger info every interval seconds
    logger = logging.getLogger(name)
    logger.record = ESPLogRecord()
    while True:
        logger.info("%s every %d seconds" % (name, interval))
        await asyncio.sleep(interval)

# main coroutine to boot async tasks
async def main():
    #logger.info("Starting WiFi")
    #ok = WiFiConnection.start_station_mode() # Use default hostname
    #w = WiFiConnection()
    #print("Result:", ok, "Info:", w.st_ssid, w.st_ip, w.hostname)

    asyncio.create_task(doSomething(2, "Task1"))

    asyncio.create_task(doSomething(7, "Task2"))

    await asyncio.sleep(1)  # Let things settle down before we get values
    
    # main task control loop pulses board led
    while True:
        logger.info("__main__: looping")
        await asyncio.sleep(5)

if __name__ == "__main__":
    
    # start asyncio task and loop
    try:
        # start the main async tasks
        asyncio.run(main())
    finally:
        # reset and start a new event loop for the task scheduler
        asyncio.new_event_loop()