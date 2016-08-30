__author__ = 'Azad'
import RPi.GPIO as GPIO
class Switching(object):

    def __init__(self, PINS):

        self.PINS = PINS
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PINS, GPIO.OUT)
        self.state =dict(zip(PINS,[0]*len(PINS)))



    def turnOn(self,position):

        self.state[position] = 1
        GPIO.output(position, GPIO.HIGH)
        print  'ON' , position

    def turnOff(self,position):


        self.state[position] = 0
        GPIO.output(position, GPIO.LOW)
        print  'Off' , position

    def getState(self):
        return self.state