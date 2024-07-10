import time
import ev3dev.ev3 as ev3

motor = ev3.LargeMotor('outA')

def set_motor_speed(speed):
    motor.run_forever(speed_sp=speed)

def stop_motor():
    motor.stop(stop_action="brake")

def water_jet(duration, speed):
    set_motor_speed(speed)
    time.sleep(duration)
    stop_motor()

def main():
    jet_duration = 5
    jet_speed = 900
    for _ in range(3):
        water_jet(jet_duration, jet_speed)
        time.sleep(2)

if __name__ == "__main__":
    main()
