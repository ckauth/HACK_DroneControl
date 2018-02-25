import PID
import ultrasonic_sensor as uss
import flight_control as fc
import startDrone
import pickle
import time
import numpy as np
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def initalise_sensors(front, left, right, rear, bottom):
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


def navigate_to_target(target_distance, sensor, control, pid, dbg_file=""):
    pid.SetPoint = target_distance
    pid.setSampleTime(0.01)

    if (dbg_file):
        distance_list = []
        time_list = []
        setpoint_list = []
        pid_list = []
        control_list = []

    # give the drone 10 seconds to complete the move
    for i in range(1, 50):
        actual_distance = sensor.distance()
        pid.update(actual_distance, 1) ####################3sensor.sign)
        pid_out = pid.output
        control_out = control.pilot_control(pid_out)

        if (dbg_file):
            distance_list.append(actual_distance)
            setpoint_list.append(pid.SetPoint)
            time_list.append(time.time())
            pid_list.append(pid_out)
            control_list.append(control_out)
            print(control_out)
        time.sleep(0.2)

    if (dbg_file):
        with open('flight_data_' + str(dbg_file) + '_.pkl', 'wb') as f:
            pickle.dump([time_list, setpoint_list, distance_list, pid_list, control_list], f)

def target_height(target_distance, dbg_file=""):
    print ('targeting bottom distance to ' + str(target_distance) + ' cm')
    navigate_to_target(
        target_distance,
        bottom_sensor,
        throttle_control,
        PID.PID(1, 0.2, 0.01),
        dbg_file)

if __name__ == "__main__":
       
    # ultrasound sensors
    front_sensor = uss.ultrasonic_sensor(11, 12, 1)
    left_sensor = uss.ultrasonic_sensor(13, 15, -1)
    right_sensor = uss.ultrasonic_sensor(16, 18, 1)
    rear_sensor = uss.ultrasonic_sensor(29, 31, -1)
    bottom_sensor = uss.ultrasonic_sensor(33, 35, 1)

    # flight controls
    throttle_control = fc.flight_control(36)
    pitch_control = fc.flight_control(37)
    roll_control = fc.flight_control(38)
    yaw_control = fc.flight_control(40)
    arm_control = fc.flight_control(32)

    # PIDs
    heightPID = PID.PID(1, 0.2, 0.01)
    rollPID = PID.PID(1, 0.2, 0.01)
    pitchPID = PID.PID(1, 0.2, 0.01)
    taxi()

    #print(startCamera())

    if (1): #startCamera()):
        #takeoff
        print('takeoff')
        navigate_to_target(70, bottom_sensor, throttle_control, heightPID, 'takeoff')

        # go forward until 1.2m from front wall
        print('forward')
        navigate_to_target(120, front_sensor, pitch_control, pitchPID, 'forward')

        # go left until 2m from right wall
        print('left')
        navigate_to_target(250, right_sensor, roll_control, rollPID, 'left')

        # go left until 1.4m from left wall
        print('more left')
        navigate_to_target(140, left_sensor, roll_control, rollPID, 'moreleft')

        print('hidden')
        # rotate 180 degrees and get images
        # TODO

        # rotate back to original position

        # go right until 2 m from left wall
        navigate_to_target(250, left_sensor, roll_control, rollPID)
        # go right until 40cm from right wal
        navigate_to_target(40, right_sensor, roll_control, rollPID)
        # go rear until 40cm from back wall
        navigate_to_target(40, rear_sensor, pitch_control, pitchPID)

        # land
        navigate_to_target(20, bottom_sensor, throttle_control, heightPID)
        navigate_to_target(10, bottom_sensor, throttle_control, heightPID)
        navigate_to_target(5, bottom_sensor, throttle_control, heightPID)
        navigate_to_target(0, bottom_sensor, throttle_control, heightPID)

    print("done")
    GPIO.cleanup()