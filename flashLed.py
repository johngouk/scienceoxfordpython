from machine import Pin, Signal

class flashLed:
    #import gc
    # red led
    # Defaults
    ledPin = Pin(2, Pin.OUT, value=1)
    led = Signal(ledPin, invert=False)
    #led = Pin(28, Pin.OUT)
    led_state = 0


    def __init__(self, pin = 2, invert = False):
        # get everything into a starting state
        # red led
        ledPin = Pin(pin, Pin.OUT, value=1)
        led = Signal(ledPin, invert)
        led_state = 0
        self.__class__.show_red_led()

    # red led handlers
    @classmethod
    def show_red_led(cls):
        cls.led.value(cls.led_state)

    @classmethod
    def toggle_red_led(cls):
        cls.led_state = 0 if cls.led_state == 1 else 1
        cls.show_red_led()

    @classmethod
    def get_red_led(cls):
        return 0 if cls.led_state == 0 else 1

    @classmethod
    def set_red_led(cls, state):
        cls.led_state = 0 if state == 0 else 1
        cls.show_red_led()
