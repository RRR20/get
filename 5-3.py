import RPi.GPIO as GPIO
import time

def db(a):
    return [int(i) for i in bin(a)[2:].zfill(bits)]

def nm(a):
    sig = db(a)
    GPIO.output(dac, sig)
    return sig


dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
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
        otv = [0]*8
        for i in range(8):
            s = [j for j in otv]
            s[i] = 1
            GPIO.output(dac, s)
            time.sleep(0.005)
            cV = GPIO.input(comp)
            if comp == 1:
                otv[i] = 1
        GPIO.output(led, otv)
        v = sum([otv[7-i]*2**i for i in range(8)])
        vol = v * mV / 256
        print('ADC value = ', v, ' -> ', otv,', input voltage = ', vol, sep = '')
except KeyboardInterrupt:
    print('\nThe program was stopped by the keyboard')
else:
    print("No exceptions")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')