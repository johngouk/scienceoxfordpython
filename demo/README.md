# Python in Education ESP Demos #
The material is intended to be used for a demo of some of the ESP32|8266 capabilities.

To use it:

1.	Edit the NetworkCredentials.py file in uploadToEsp/ for your network
2.	Upload all the material in uploadToEsp/ to / on the ESP filesystem
3.	Use the importLogging.py script to install some additional micropython-lib libs
4.	Try some of the scripts in this folder, following the Word doc in the main filder above this


*	asyncioDemo.py - quick demo of 'asyncio'
*	basicLogging.py - demo MPy use of 'logging' module
*	betterLogging.py - uses an improved ESP-specific LogRecord implementation
*	checkPyImplementation.py - sample code to chek what ESP and Python version
*	importLogging.py - Example of using 'mip' to install some libs
*	logDataToCSV.py - demo of logging data to a CSV in ESP filesystem
*	moreAdvancedSTAConnect.py - you did edit the NetworkCredentials file, didn't you??
*	simpleAPMode.py - use the ESP as an Access Point
*	simpleLCD.py - connect an I2C LCD1602 and go for it
*	simpleSTAConnect.py - like we said, you did edit the NetworkCredentials file, didn't you??