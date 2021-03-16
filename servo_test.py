import time
import board
import pwmio
from adafruit_motor import servo
from adafruit_servokit import ServoKit

# create a PWMOut object on Pin A2.
# pwm = pwmio.PWMOut(board.A11, duty_cycle=2 ** 15, frequency=50)
kit = ServoKit(channels=16)
# Create a servo object, my_servo.
# my_servo = servo.Servo(pwm)
my_servo = kit.servo[13]

# while True:
#     for angle in range(45, 135, 5):  # 0 - 180 degrees, 5 degrees at a time.
#         my_servo.angle = angle
#         time.sleep(0.05)
#     for angle in range(135, 45, -5):  # 180 - 0 degrees, 5 degrees at a time.
#         my_servo.angle = angle
#         time.sleep(0.05)

upper_camera = kit.servo[13]
time.sleep(1)
upper_camera.angle = 45
time.sleep(1)
upper_camera.angle = 180

lower_camera = kit.servo[1]
time.sleep(1)
lower_camera.angle = 0
time.sleep(1)
lower_camera.angle = 180
time.sleep(1)
lower_camera.angle = 90

