from BLE import BLEPeripheral
from ssd1306 import SSD1306_I2C
from machine import I2C, Pin
import time

sdaPin = Pin(21, Pin.OUT)
sclPin = Pin(22, Pin.OUT)

i2c = I2C(scl=sclPin, sda=sdaPin)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("3D Scanner", 0, 56)
oled.show()


def bleOnReadCallback(data):
    print(data)
    oled.fill(0x0000)
    oled.text(data, 0, 56)
    oled.show()

def rmSpecChars(string):
    

ble = BLEPeripheral(name="Scanner")
ble.on_write(bleOnReadCallback)
