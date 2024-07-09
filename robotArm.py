from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, ColorSensor
from ev3dev2.led import Leds
import time


motor_a = LargeMotor(OUTPUT_A)
motor_b = LargeMotor(OUTPUT_B)
motor_c = LargeMotor(OUTPUT_C)
motor_d = LargeMotor(OUTPUT_D)


touch_sensor = TouchSensor(INPUT_1)
color_sensor = ColorSensor(INPUT_2)


leds = Leds()


    # Start motors A and B in a tank movement
    tank = MoveTank(OUTPUT_A, OUTPUT_B)
    tank.on_for_seconds(SpeedPercent(50), SpeedPercent(50), 2)
    
    # Reverse motors A and B
    tank.on_for_seconds(SpeedPercent(-50), SpeedPercent(-50), 2)

    # Turn on motor C for 3 seconds
    motor_c.on_for_seconds(SpeedPercent(50), 3)
    
    # Turn on motor D for 3 seconds in reverse
    motor_d.on_for_seconds(SpeedPercent(-50), 3)

def sensor_check():
    # Check touch sensor status
    if touch_sensor.is_pressed:
        leds.set_color('LEFT', 'RED')
        leds.set_color('RIGHT', 'RED')
        print("Touch sensor pressed")
    else:
        leds.set_color('LEFT', 'GREEN')
        leds.set_color('RIGHT', 'GREEN')
        print("Touch sensor not pressed")

    # Check color sensor
    color = color_sensor.color
    if color == ColorSensor.COLOR_RED:
        print("Red color detected")
    elif color == ColorSensor.COLOR_BLUE:
        print("Blue color detected")
    else:
        print("Other color detected")

def combined_action():
    # Run motor sequence
    motor_sequence()
    
    # Check sensors
    sensor_check()

    # Wait for a touch sensor press
    print("Waiting for touch sensor press...")
    touch_sensor.wait_for_pressed()
    print("Touch sensor pressed, starting motor sequence again")
    
    # Run motor sequence again
    motor_sequence()

def main():
    while True:
        combined_action()
        time.sleep(5)  # Wait for 5 seconds before repeating

if __name__ == '__main__':
    main()
