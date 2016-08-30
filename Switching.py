__author__ = 'Azad'
import RPi.GPIO as GPIO


class Switching(object):
    def __init__(self, pins):
        GPIO.cleanup()
        self.pins = pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pins, GPIO.OUT)
        self.state = dict(zip(pins, [0] * len(pins)))

    def turn_on(self, position):
        self.state[position] = 1
        GPIO.output(position, GPIO.HIGH)
        print 'ON', position

    def turn_off(self, position):
        self.state[position] = 0
        GPIO.output(position, GPIO.LOW)
        print 'Off', position

    def get_state(self):
        x = [str(self.state[x]) for x in self.pins]
        x = ''.join(x)
        return x
