__author__ = 'Azad'
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

PORT1 = (3, 5, 7)
PORT2 = (33, 35, 37)
PORT3 = (26, 24, 22)

PORT = (PORT1, PORT2, PORT3)

BLUE, GREEN, RED = zip(PORT1, PORT2, PORT3)

GPIO.setup(PORT1 + PORT2 + PORT3, GPIO.OUT)


def wave(color, times = 5, hz = 100):

    val = [item for sublist in color for item in sublist]
    pulse_pin = [GPIO.PWM(y, hz) for y in val]

    for x in pulse_pin:
        x.start(0)

    init = 0

    while init < times:
        for dc in range(0, 101, 1):
            for p in pulse_pin:
                p.ChangeDutyCycle(dc)
                time.sleep(0.01)
        for dc in range(100, -1, -1):
            for p in pulse_pin:
                p.ChangeDutyCycle(dc)
                time.sleep(0.01)
        init = init + 1
    for p in pulse_pin:
        p.stop()




times = [2, 3]
pluses = [100, 50, 10]

colors = [RED, BLUE, GREEN]

combinations = list(((color,c_time,pluse) for c_time in times for pluse in pluses for color in colors))

while True:
    try:
        for x in combinations:
            (color, c_time, pluse) = x
            wave([color], c_time, pluse)

    except KeyboardInterrupt:
        print ('AAAA')
        break
GPIO.cleanup()