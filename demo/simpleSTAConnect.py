
import network, time

from NetworkCredentials import NetworkCredentials


# Connection
w = network.WLAN(network.STA_IF)
w.active(True)
print("Let's see who's around...")
networkList = w.scan()
for n in networkList:
    print('SSID', n[0],'RSSI',n[3])
print("Attempting connect to %s..."%(NetworkCredentials.ssid))
# This approach to waiting for a connection is safer because otherwise
# it loops forever if the SSID/AP doesn't exist or the password is wrong!
start = time.ticks_ms()
w.connect(NetworkCredentials.ssid, NetworkCredentials.password)
count = 0 
while not (w.isconnected()) and count < 20:
    count += 1
    time.sleep(0.5) # Sleept for 0.5 secs
end = time.ticks_ms()

if w.isconnected():
    ipaddr = w.ifconfig()[0]
    # Need this to connect!!
    print('Connected! SSID: %s Hostname: %s IP: %s taking %d msecs' % (NetworkCredentials.ssid, network.hostname(), ipaddr, time.ticks_diff(end, start)))   
else:
    print(("Error connecting to SSID %s - state: %s") % (NetworkCredentials.ssid,statusCodes[w.status()]))
