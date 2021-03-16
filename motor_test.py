import time
import RPi.GPIO as gpio
#from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685
import busio
import board

#pca = ServoKit(channels=16)
#pwm = adafruit_pca9685.PCA9685()

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)

# Pins Motor A RPI GPIO
AIN1 = 17
AIN2 = 18

# Pins Motor A RPI GPIO
BIN1 = 27
BIN2 = 22

# Pin Motor A PCA
pwma = pca.channels[4]
# Pin Motor B PCA
pwmb = pca.channels[6]

pca.frequency = 60

# pwma.duty_cycle = 0xffff #high
# pwmb.duty_cycle = 0xffff #high

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(AIN1, gpio.OUT)
gpio.setup(AIN2, gpio.OUT)
gpio.setup(BIN1, gpio.OUT)
gpio.setup(BIN2, gpio.OUT)

gpio.output(AIN1, gpio.LOW)
gpio.output(AIN2, gpio.HIGH)

gpio.output(BIN1, gpio.LOW)
gpio.output(BIN2, gpio.HIGH)

time.sleep(0.5)

gpio.cleanup()

