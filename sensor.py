import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 22
ECHO = 23

print "Distance measurement in progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for sensor to settle"
time.sleep(2)

def distance():

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    #print pulse_duration
    #print pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print "distance:", distance, "cm"

if __name__ == '__main__':
    try:
        while True:
            distance()
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
