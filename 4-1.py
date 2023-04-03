import RPi.GPIO as gpio
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
    while True:
        x = input('Введите целое число от 0 до 255 (или q для выхода: ')
        if x.isdigit() and x == int(x):
            if int(x) >= 0 and int(x) <= 255:
                gpio.output(dac, from10to2(x))
                voltage = (x/256)*3.3
                print(voltage)
            else:
                print('Введенное число не попадает в заданный диапазон!')
                continue
        elif x == 'q':
            break
        else: print('Вы, многоуважаемый, читать не умеете?')

finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup(dac)