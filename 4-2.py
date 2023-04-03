import RPi.GPIO as gpio
import time
dac = [] # список портов в области DAC
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def from10to2(x):
    x_new = bin(x)
    l = []
    for i in x_new:
        l.append(i)
    l.pop(0)
    l.pop(0)
    return l

try:
    t = int(input('Введите период: '))
    i = 0
    for i in range(0, 255):
        i += 1
        gpio.output(dac, from10to2(i))
        time.sleep(t/512)
    for i in range(0, 255):
        i -= 1
        gpio.output(dac, from10to2(i))
        time.sleep(t/512)

finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup(dac)