from ev3dev2.motor import LargeMotor, OUTPUT_A
from ev3dev2.motor import SpeedPercent

# Initialize the motor connected to port A
motor = LargeMotor(OUTPUT_A)

# Set the motor to run at 100% speed
motor.on(SpeedPercent(100))
