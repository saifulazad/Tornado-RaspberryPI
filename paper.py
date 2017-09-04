import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

LEDS = (7, 10, 12, 16, 18, 22, 24, 26)


GPIO.setup(LEDS, GPIO.OUT)

def work(val = True):
    for pin in LEDS:
        GPIO.output(pin, val)
        time.sleep(1)
        GPIO.output(pin, False)
        time.sleep(1)

    for pin in LEDS:
        GPIO.output(pin, False)


while True:
    try:
        work();
        # work(False)
    except KeyboardInterrupt:
        break
GPIO.cleanup()