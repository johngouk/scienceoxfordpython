
import network, time
import os
if "ESP32" in os.uname().machine:
    ESP32 = True
else:
    ESP32 = False
from micropython import const

from NetworkCredentials import NetworkCredentials

# Taken from ESP32 Micropython network module
statusCodes = {
    network.STAT_IDLE:const("IDLE"),
    network.STAT_CONNECTING:const("CONNECTING"),
    network.STAT_GOT_IP:const("GOT_IP"),
    network.STAT_IDLE:const("IDLE"),
    network.STAT_NO_AP_FOUND:const("NO_AP_FOUND - check SSID"),
    network.STAT_WRONG_PASSWORD:const("WRONG_PASSWORD"),
    }
if ESP32:
    statusCodes[network.STAT_ASSOC_FAIL] = const("ASSOC_FAIL")
    statusCodes[network.STAT_BEACON_TIMEOUT] = const("BEACON_TIMEOUT")
    statusCodes[network.STAT_HANDSHAKE_TIMEOUT] = const("HANDSHAKE_TIMEOUT")


# Connection
w = network.WLAN(network.STA_IF)
w.active(True)

# The ESP32 will try to reconnect if you only did a soft MPy reset, so don't try
# if you're already connected
if not w.isconnected():
    w.disconnect() # Just in case there was a previou attempt...
    print("Attempting connect...")
    w.connect(NetworkCredentials.ssid, NetworkCredentials.password)
    # This approach to waiting for a connection is safer because otherwise
    # it loops forever if the SSID/AP doesn't exist or the password is wrong!
    count = 0 
    while not (w.isconnected()) and count < 20:
        count += 1
        time.sleep(0.5) # Sleept for 0.5 secs

if w.isconnected():
    ipaddr = w.ifconfig()[0]
    print('Connected! IP: ' + ipaddr)   # Need this to connect!!
    print('Hostname:', network.hostname())
else:
    print(("Error connecting - state: %s") % statusCodes[w.status()])
