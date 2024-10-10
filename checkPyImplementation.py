# Handy script for checking target implementation
import sys
if sys.implementation.name == "micropython":
    print("micropython")
#     Do something     
elif sys.implementation.name == "cpython":
    print("lappie")
#     Do something     
    
import os
if "ESP32" in os.uname().machine:
    print("ESP32")
#     Do something     
    if "S3" in os.uname().machine:
        print("S3")
#     Do something     
elif "ESP8266" in os.uname().machine:
    print ("ESP8266")
#     Do something     
