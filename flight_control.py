import RPi.GPIO as GPIO

class flight_control:

    def __init__(self, pwm_pin):

        self.pwm_pin = pwm_pin
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.control = GPIO.PWM(self.pwm_pin, 50)
        self.pilot_control(0)

    def pilot_control(self, duty_cycle):
        #print("dc " + str(duty_cycle))
        if duty_cycle > 500:
            duty_cycle = 500
        if duty_cycle < -500:
            duty_cycle = 500
        self.control.start(7.5 + duty_cycle/200) # duty cycle in percent
        return 1500 + duty_cycle
