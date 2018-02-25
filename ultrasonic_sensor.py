import RPi.GPIO as GPIO
import time

class ultrasonic_sensor:

    def __init__(self, trig_pin, echo_pin, sign):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.sign = sign

        GPIO.setup(trig_pin, GPIO.OUT)
        GPIO.output(trig_pin, False)
        GPIO.setup(echo_pin, GPIO.IN)

    def distance(self):
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        pulse_start = time.time()
        pulse_end = pulse_start
        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150 # check this factor
        distance = round(distance, 0)
        return distance

