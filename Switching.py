__author__ = 'Azad'
import RPi.GPIO as GPIO

BOARD_PINS = [3]
class Switching(object):

    def __init__(self):


        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(BOARD_PINS, GPIO.OUT)
        self.state =[0]*4


    def turnOn(self,position):

        self.state[position] = 1
        GPIO.output(position, GPIO.HIGH)
        print  'ON' , position

    def turnOff(self,position):


        self.state[position] = 0
        GPIO.output(position, GPIO.LOW)
        print  'Off' , position

