import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

#обработка
def db(a):
    return [int(i) for i in bin(a)[2:].zfill(bits)]

def nm(a):
    sig = db(a)
    GPIO.output(dac, sig)
    return sig

def U():
        for i in range(8):
            s = [j for j in otv]
            s[i] = 1
            GPIO.output(dac, s)
            time.sleep(0.005)
            cV = GPIO.input(comp)
            if cV == 1:
                otv[i] = 1

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
bits = 8
mV = 3.3
tM = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(tM, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

t1 = time.time()
vol = 0
try:
    rm = [0]
    c = 0
    #зарядка
    GPIO.output(17, 0)
    while vol < 3:
        otv = [0]*8
        U()
        GPIO.output(led, otv)
        v = sum([otv[7-i]*2**i for i in range(8)])
        vol = v * mV / 256
        rm.append(vol)
        c += 1
        print('ADC value = ', v, ' -> ', otv,', input voltage = ', vol, sep = '')   
         #разрядка
    print('зарядка окончена')
    GPIO.output(17, 1)
    while vol>1 :
        otv = [0]*8
        U()
        GPIO.output(led, otv)
        v = sum([otv[7-i]*2**i for i in range(8)])
        vol = v * mV / 256
        rm.append(vol)
        c += 1
        print('ADC value = ', v, ' -> ', otv,', input voltage = ', vol, sep = '')
    print('Разрядка окончена')
    t2 = time.time()
    #запись в файл
    with open('data.txt', 'w') as f:
        for i in rm:
            f.write(str(i)+'\n')
        f.write(str(1/(t2-t1)/c))
    print('Общая продолжительность эксперимента:', t2-t1)
    print('Средняя частота дискретизации:', 1/(t2-t1)/c)
    #построение графика
    y = [i for i in rm]
    x = [i*(t2-t1)/c for i in range(len(rm))]
    plt.plot(x,y)
    plt.show()

except KeyboardInterrupt:
    GPIO.output(tM, 0)
    print('\nThe program was stopped by the keyboard')
else:
    print("No exceptions")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    print('GPIO cleanup completed')