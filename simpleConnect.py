import network

# Connection
w = network.WLAN(network.STA_IF)
w.active(True)
w.connect("ssid", "password")
while not (w.isconnected()):
    pass
ipaddr = w.ifconfig()[0]
print('Connected! IP: ' + ipaddr)   # Need this to connect!!
print('Hostname:', network.hostname())
