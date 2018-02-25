import PID
import ultrasonic_sensor as uss
import flight_control as fc
from  startDrone import *
import pickle
import time
import numpy as np
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# pins should be globally initialised

def initalise_sensors(front, left, right, rear, bottom):
    # ultrasound sensors
    global front_sensor, rear_sensor, left_sensor, right_sensor, bottom_sensor
    front_sensor = uss.ultrasonic_sensor(front)
    left_sensor = uss.ultrasonic_sensor(left)
    right_sensor = uss.ultrasonic_sensor(right)
    rear_sensor = uss.ultrasonic_sensor(rear)
    bottom_sensor = uss.ultrasonic_sensor(bottom)

def taxi():
    print ("taxi")
 
    # to arm the drone, arm & trottle must be minimal, all others medium
    throttle_control.pilot_control(-510)
    arm_control.pilot_control(-510)
    pitch_control.pilot_control(0)
    roll_control.pilot_control(0)
    yaw_control.pilot_control(0)
    time.sleep(2)

    # pull arm to maximum and we can start
    arm_control.pilot_control(510)
    time.sleep(2)


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

# desired distance in coordinate system relative to current orientation of drone
def move(x, y):
    # get current position
    dfront = front_sensor.distance()
    dback = rear_sensor.distance()
    dleft = left_sensor.distance()
    dright = right_sensor.distance()

    gfront = dfront - y
    gback = dback + y
    gleft = dleft + x
    gright = dright - x

    # need feedback loop to determine pitch and roll

if __name__ == "__main__":
    
    # ultrasound sensors
    front = (11, 12)
    left = (13, 15)
    right = (16, 18)
    rear = (29, 31)
    bottom = (33, 35)
    initialise_sensors(front, left, right, rear, bottom)

    '''
    # ultrasound sensors
    #front_sensor = uss.ultrasonic_sensor(17, 18)
    #left_sensor = uss.ultrasonic_sensor(27, 22)
    #right_sensor = uss.ultrasonic_sensor(23, 24)
    #rear_sensor = uss.ultrasonic_sensor(5, 6)
    #bottom_sensor = uss.ultrasonic_sensor(13, 19)
    bottom_sensor = uss.ultrasonic_sensor(33, 35)'''

    # flight controls
    #throttle_control = fc.flight_control(16)
    throttle_control = fc.flight_control(36)
    pitch_control = fc.flight_control(37)
    roll_control = fc.flight_control(38)
    yaw_control = fc.flight_control(40)
    #GPIO.setmode(GPIO.BOARD)
    arm_control = fc.flight_control(32)
    #arm_control = fc.flight_control(12)

    taxi()

    if (1): #startCamera()):
        takeoff(
            70.0,
            bottom_sensor,
            PID.PID(1, 0.2, 0.01),1)

        takeoff(
            100.0,
            bottom_sensor,
            PID.PID(1, 0.2, 0.01),2)

        takeoff(
            70.0,
            bottom_sensor,
            PID.PID(1, 0.2, 0.01),3)




    print("done")
    GPIO.cleanup()