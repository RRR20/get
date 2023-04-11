import RPi.GPIO as GPIO
import time

def db(a):
    return [int(i) for i in bin(a)[2:].zfill(bits)]

def nm(a):
    sig = db(a)
    GPIO.output(dac, sig)
    return sig


dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = 8
mV = 3.3
tM = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, inintal = GPIO.LOW)
GPIO.setup(tM, GPIO.OUT, inital = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        for v in range(255):
            vol = v*mV/256
            sig = nm(v)
            time.sleep(0.005)
            cV = GPIO.input(comp)
            if cV == 0:
                print('ADC value = ', v, ' -> ', sig,', input voltage = ', vol, sep = '')
                break
except KeyboardInterrupt:
    print('\nThe program was stopped by the keyboard')
else:
    print("No exceptions")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')