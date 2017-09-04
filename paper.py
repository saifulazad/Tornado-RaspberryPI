import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

LEDS = (7, 10, 12, 16, 18, 22, 24, 26)


GPIO.setup(LEDS, GPIO.OUT)

def work(val = True):
    for pin in LEDS:
        GPIO.output(pin, val)
        time.sleep(1)


while True:
    try:
        work(True);
        work(False)
    except KeyboardInterrupt:
        break
GPIO.cleanup()