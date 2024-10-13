"""

    simpleLCD.py
    Demo the LCD1602 display.
    I put a wrapper (LCD) around the esp8266_i2c_lcd module to make it simpler to setup, and hide the
    construction of the I2C connection.
    Before running this, load the following files on to the ESP FS root:
        esp8266_i2c_lcd.py
        LCD.py
        lcd_api.py
        ESPLogRecord.py
    You need an HD44780 character LCD connected via PCF8574 on I2C on GPIO port 26
    to make this work, or use a different pin by changing the LCD() constructor params
    (i2c=0, sclPin=18, sdaPin=19, columns=16, lines=2)
    where
        i2c is the ESP32 I2C unit id [0|1]

"""
import time

from LCD import LCD

lcd = LCD() # Initialise
lcd.move_to(0,0) # Top left
#			0         1   0         1
#			012345678901  01234567890123456
lcd.putstr('Yo from ESP!\nFeels good!')
time.sleep(5)
lcd.clear()

while True:
    ns = time.time_ns()
    # 000000000011111111
    # 012345678901234567
    # SSSSSSSSSMMMIIINNN
    sNs = str(ns)
    # YYYY-MM-DD HH:MM" 16 chars
    dateTime = time.strftime('%Y-%m-%d,%H:%M:%S',time.gmtime(int(sNs[0:9])))
    # SSSSSSSSS.MMMIII" 16 chars
    secsMillisMicros = '%d.%d%d'%(int(sNs[0:9]), int(sNs[9:12]), int(sNs[12:15]))
    lcd.move_to(0,0)
    lcd.putstr(dateTime)
    lcd.move_to(0,1)
    lcd.putstr(secsMillisMicros)
    time.sleep_ms(1000)
    