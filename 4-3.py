import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    p = GPIO.PWM(24, 1000)
    p.start(0)
    print(3.3)
    while True:
        t = float(input('dc(0-100%) = '))
        p.ChangeDutyCycle(t)
        print(3.3*t/100)

finally:
    p.stop()
    GPIO.out(24, 0)
    GPIO.clean()