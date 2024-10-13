# AP Mode example - try accessing the AP using the SSID and password!
import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
# The following additional config allows overly smart devices like iPhones to connect
# otherwise they get upset about no security and no password!
password = 'thepassword'
ap.config(authmode=network.AUTH_WPA_WPA2_PSK, password=password)
ap_ip = ap.ifconfig()[0]
ap_ssid = ap.config('ssid')
print("SSID: %s Password:'%s' IP:%s" % (ap_ssid, password, ap_ip))