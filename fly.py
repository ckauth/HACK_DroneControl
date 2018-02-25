import PID
import ultrasonic_sensor as uss
import flight_control as fc
from  startDrone import *
import pickle
import time
import numpy as np
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def taxi():
    print ("taxi")
 
    # to arm the drone, arm & trottle must be minimal, all others medium
    throttle_control.pilot_control(-500)
    arm_control.pilot_control(-500)
    time.sleep(2)

    # pull arm to maximum and we can start
    arm_control.pilot_control(500)
    

def takeoff(target_height, sensor, pid, index):
    print ("takeoff")
    pid.SetPoint = target_height
    pid.setSampleTime(0.01)

    actualheight_list = []
    time_list = []
    setpoint_list = []
    pidout_list = []
    trottleout_list = []

    for i in range(1, 50):
        actual_height = sensor.distance()
        pid.update(actual_height)
        pid_out = pid.output
        trottle_out = throttle_control.pilot_control(pid_out)
        print(trottle_out)
        time.sleep(0.2)

        actualheight_list.append(actual_height)
        setpoint_list.append(pid.SetPoint)
        time_list.append(i)
        pidout_list.append(pid_out)
        trottleout_list.append(trottle_out)

    with open('flight_data.pkl' + str(index), 'wb') as f:
        pickle.dump([time_list, setpoint_list, actualheight_list, pidout_list, trottleout_list], f)

if __name__ == "__main__":
    
    # ultrasound sensors
    front_sensor = uss.ultrasonic_sensor(17, 18)
    left_sensor = uss.ultrasonic_sensor(27, 22)
    right_sensor = uss.ultrasonic_sensor(23, 24)
    rear_sensor = uss.ultrasonic_sensor(5, 6)
    bottom_sensor = uss.ultrasonic_sensor(13, 19)

    # flight controls
    throttle_control = fc.flight_control(16)
    pitch_control = fc.flight_control(26)
    roll_control = fc.flight_control(20)
    yaw_control = fc.flight_control(21)
    arm_control = fc.flight_control(12)

    taxi()

    if (1): #startCamera()):
        takeoff(
            70.0,
            bottom_sensor,
            PID.PID(5, 0.5, 0.05),1)

        takeoff(
            100.0,
            bottom_sensor,
            PID.PID(5, 0.5, 0.05),2)

        takeoff(
            70.0,
            bottom_sensor,
            PID.PID(5, 0.5, 0.05),3)

    print("done")
    GPIO.cleanup()