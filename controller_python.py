import RPi.GPIO as GPIO
import time

def control_dc(dc_in):
    power_dc.start(dc_in) # percentage of duty cycle
    time.sleep(2) # do what you do for given amount of seconds



GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
# determines which pin set is being used 

PIN_POWER = 16

GPIO.setup(PIN_POWER, GPIO.OUT)

power_dc = GPIO.PWM(PIN_POWER, 1) # first trial value: 500 Hz

initial_dc = 50 # initial value
final_dc = 0
decrement = -10

for dc_in in range(initial_dc, final_dc, decrement):
    control_dc(dc_in)
    print "current dc:", dc_in

power_dc.stop()

GPIO.cleanup()


