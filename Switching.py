__author__ = 'Azad'
import RPi.GPIO as GPIO

class Switching(object):

    def __init__(self, PINS):

        self.PINS = PINS
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PINS, GPIO.OUT)
        self.state =[0]*4
        self.offset = 10


    def turnOn(self,position):

        self.state[position - self.offset] = 1
        GPIO.output(position, GPIO.HIGH)
        print  'ON' , position

    def turnOff(self,position):


        self.state[position - self.offset] = 0
        GPIO.output(position, GPIO.LOW)
        print  'Off' , position

