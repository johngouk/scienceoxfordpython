# Uses mip to import mP logging module
import network, mip
    
import NetCreds

# Connection
w = network.WLAN(network.STA_IF)
w.active(True)
w.connect(NetCreds.ssid, NetCreds.password)
while not (w.isconnected()):
    pass
ipaddr = w.ifconfig()[0]
print('Connected! IP: ' + ipaddr)   # Need this to connect!!

mip.install('logging')
mip.install('time')
