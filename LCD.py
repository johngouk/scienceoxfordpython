"""
    LCD - script to provide access to a LCD1602 SPI-attached display

    LCD Operations

    def clear()        Clears the LCD display and moves the cursor to the top left corner.
    def show_cursor()       Causes the cursor to be made visible.
    def hide_cursor()       Causes the cursor to be hidden.
    def blink_cursor_on()       Turns on the cursor, and makes it blink.
    def blink_cursor_off()       Turns on the cursor, and makes it no blink (i.e. be solid).
    def display_on()       Turns on (i.e. unblanks) the LCD.
    def display_off()       Turns off (i.e. blanks) the LCD.
    def backlight_on()       Turns the backlight on. This isn't really an LCD command, but some modules have backlight controls.
    def backlight_off()       Turns the backlight off. This isn't really an LCD command, but some modules have backlight controls.
    def move_to(cursor_x, cursor_y)       Moves the cursor position to the indicated position. The cursor position is zero based (i.e. cursor_x == 0 indicates first column).
    def putchar(char)       Writes the indicated character to the LCD at the current cursor position, and advances the cursor by one position.
    def putstr(string)       Write the indicated string to the LCD at the current cursor position and advances the cursor position appropriately.

"""
from micropython import const
from machine import Pin
from machine import I2C
# LCD Libraries need to be copied to Flash
import time, asyncio
import logging

logger = logging.getLogger(__name__)
from ESPLogRecord import ESPLogRecord
logger.record = ESPLogRecord()

from esp8266_i2c_lcd import I2cLcd


class LCD(I2cLcd):

    DEFAULT_I2C_ADDR = 0x27
    DEFAULT_I2C_FREQ = 100000

    def __init__(self, i2c=0, sclPin=18, sdaPin=19, columns=16, lines=2):
        logger.info(const("initialising LCD: I2C: %d SCL: %d SDA: %d freq: %d col: %d lines: %d"),
                    i2c, sclPin, sdaPin, LCD.DEFAULT_I2C_FREQ, columns, lines)
        self.sdaPin = sdaPin
        self.sclPin = sclPin
        self.i2cUnit = i2c
        self.scl = Pin(self.sclPin, Pin.PULL_UP)
        self.sda = Pin(self.sdaPin, Pin.PULL_UP)
        self.l = lines
        self.c = columns
        super().__init__(I2C(self.i2cUnit, scl=self.scl, sda=self.sda, freq=LCD.DEFAULT_I2C_FREQ),
                             LCD.DEFAULT_I2C_ADDR, lines, columns)

    # Horrible function that does something until I find a better I2C LCD implementation...
    async def updateLCD(self, interval, line0, line1):
        blank = const('                ')
        while True:
            self.move_to(0,0) # use first row
            self.putstr(blank)
            self.move_to(0,0) # use first row
            self.putstr(line0())
            
            self.move_to(0,1) # use second row
            self.putstr(blank)
            self.move_to(0,1) # use second row
            self.putstr(line1())
            await asyncio.sleep(interval)

async def main():
    import random
    def line0():
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    
    def line1():
        return str(random.randint(1,10000))
    
    asyncio.create_task(lcd.updateLCD(5, line0, line1))
    while True:
        logger.info("LCD test main looping...")
        await asyncio.sleep(30)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s')
    logger.info("Starting LCD Demo")
    lcd = LCD() # Use the defaults
    
    lcd.putstr("Hi there!\nThis is an LCD")

    # start asyncio task and loop
    try:
        # start the main async tasks
        asyncio.run(main())
    finally:
        # reset and start a new event loop for the task scheduler
        asyncio.new_event_loop()
