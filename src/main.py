from BLE import BLEPeripheral
from ssd1306 import SSD1306_I2C
from machine import I2C, Pin
from Stepper import Stepper
import time

# Oled setup
sdaPin = Pin(21, Pin.OUT)
sclPin = Pin(22, Pin.OUT)

i2c = I2C(scl=sclPin, sda=sdaPin)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("3D Scanner", 0, 56)
oled.show()


def logToOled(string):
    oled.fill(0x0000)
    oled.text(string, 0, 28)
    oled.show()


# BLE setup
def bleOnWriteCallback(data):
    data = data.decode("utf-8")
    data = removeSpecialCharacters(data)
    print(data)
    logToOled(data)
    doAction(data)
    ble.send("OK")


ble = BLEPeripheral(name="Scanner")
ble.on_write(bleOnWriteCallback)

# Stepper setup
stepperPins = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(27, Pin.OUT)]

stepper = Stepper(
    "HALF_STEP", stepperPins[0], stepperPins[1], stepperPins[2], stepperPins[3], 1
)


# action consist of command and value
# example "TL-5" - turn left 5 degrees
# actions : TL - turn left
#           TR - turn right
def doAction(action: str):
    command, value = parseAction(action)

    print("doAction", action, command, value)

    if command == "TR":
        stepper.angle(value, direction=1)
    elif command == "TL":
        stepper.angle(value, direction=-1)
    else:
        raise Exception("Incorrect command")


def parseAction(action):
    action = action.split("-")
    return (action[0], int(action[1]))


def removeSpecialCharacters(string):
    specialChars = ["\n", "\r"]
    buf = str()
    for char in string:
        if char not in specialChars:
            buf += char
    return buf

