
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

PORT1 = (3, 5, 7)
PORT2 = (33, 35, 37)
PORT3 = (26, 24, 22)

PORT = (PORT1, PORT2, PORT3)

BLUE, GREEN, RED = zip(PORT1, PORT2, PORT3)

# RED = []
GPIO.setup(PORT1 + PORT2 + PORT3, GPIO.OUT)


def wave(color):
    pulse_pin = [GPIO.PWM(x, 100) for x in color]

    #p = GPIO.PWM(BLUE, 5)  # channel=12 frequency=50Hz
    #p.start(0)
    for x in pulse_pin:
        x.start(0)
    times = 5
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


while True:
    try:
        wave(BLUE)
        wave(RED)
        wave(GREEN)
    except KeyboardInterrupt:
        break
GPIO.cleanup()
