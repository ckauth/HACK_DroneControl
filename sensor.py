import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 13
ECHO = 19

print "Distance measurement in progress"

def us_setup(trig_pin, echo_pin): # setup for ultrasonic sensors
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    
    GPIO.output(trig_pin, False) # switch output off for safety
    return trig_pin, echo_pin

def distance(us_sensor):
    trig, echo = us_sensor
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150 # check this factor
    distance = round(distance, 2)
    return distance

def teardown():
    GPIO.cleanup()

if __name__ == '__main__':
    trig = 13
    echo = 19
    us5 = us_setup(trig, echo)

    try:
        while True:
            distance = distance(us5)
            print 'distance:', distance, 'cm'
            time.sleep(0.5)

    except KeyboardInterrupt:
        teardown()
