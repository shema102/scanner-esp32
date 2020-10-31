# import bluetooth_demo

# bluetooth_demo.demo()

import time
from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

sdaPin = Pin(21, Pin.OUT)
sclPin = Pin(22, Pin.OUT)

i2c = I2C(scl=sclPin, sda=sdaPin)
oled = SSD1306_I2C(128, 64, i2c)
