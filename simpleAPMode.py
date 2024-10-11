# AP Mode example - try accessing the AP using the SSID!
import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap_ip = ap.ifconfig()[0]
ap_ssid = ap.config('ssid')
print("SSID:", ap_ssid, "IP:", ap_ip)