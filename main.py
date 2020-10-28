import Stepper
from machine import Pin

"""
IN1 -->  13
IN2 -->  12
IN3 -->  14
IN4 -->  27
"""
s1 = Stepper.create(
    Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(27, Pin.OUT), delay=2
)
s1.step(100)
s1.step(100, -1)
s1.angle(180)
s1.angle(360, -1)

