import time
import RPi.GPIO as gpio
from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685
import busio
import board
import adafruit_motor.servo

kit = ServoKit(channels=16)
# servo = adafruit_motor.servo.Servo(servo_channel)
# pwm = adafruit_pca9685.PCA9685()

kit.servo[11].actuation_range = 90
kit.servo[11].angle = 0
# # kit.continuous_servo[1].throttle = 0
# time.sleep(1)
# # kit.continuous_servo[1].throttle = 0
# kit.servo[11].angle = 90
# # kit.continuous_servo[1].throttle = 0

# Pins Motor A RPI GPIO
AIN1 = 17
AIN2 = 18
# Pins Motor A RPI GPIO
BIN1 = 27
BIN2 = 22


def init():
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = PCA9685(i2c)
    # Pin Motor A PCA
    pwma = pca.channels[4]
    # Pin Motor B PCA
    pwmb = pca.channels[5]
    # Vitesse ?
    pca.frequency = 60

    # Je ne sais pas à quoi ça sert et ça fonctionne sans pour le moment
    # pwma.duty_cycle = 0xffff #high
    # pwmb.duty_cycle = 0xffff #high

    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)

    gpio.setup(AIN1, gpio.OUT)
    gpio.setup(AIN2, gpio.OUT)
    gpio.setup(BIN1, gpio.OUT)
    gpio.setup(BIN2, gpio.OUT)


def forward(tf):
    init()
    gpio.output(AIN1, gpio.LOW)
    gpio.output(AIN2, gpio.HIGH)
    gpio.output(BIN1, gpio.LOW)
    gpio.output(BIN2, gpio.HIGH)
    # TF : Time Frame
    time.sleep(tf)
    gpio.cleanup()


def backward(tf):
    init()
    gpio.output(AIN1, gpio.HIGH)
    gpio.output(AIN2, gpio.LOW)
    gpio.output(BIN1, gpio.HIGH)
    gpio.output(BIN2, gpio.LOW)
    time.sleep(tf)
    gpio.cleanup()


def reverse_left(tf):
    init()
    gpio.output(AIN1, gpio.HIGH)
    gpio.output(AIN2, gpio.LOW)
    gpio.output(BIN1, gpio.LOW)
    gpio.output(BIN2, gpio.HIGH)
    time.sleep(tf)
    gpio.cleanup()


def reverse_right(tf):
    init()
    gpio.output(AIN1, gpio.LOW)
    gpio.output(AIN2, gpio.HIGH)
    gpio.output(BIN1, gpio.HIGH)
    gpio.output(BIN2, gpio.LOW)
    time.sleep(tf)
    gpio.cleanup()


# forward(1)
# time.sleep(1)
# backward(1)
# time.sleep(1)
# reverse_left(1)
# time.sleep(1)
# reverse_right(1)
