#!/bin/bash
sshpass -p swissless scp PID.py pi@130.82.238.173:flightcontrol/.
sshpass -p swissless scp ultrasonic_sensor.py pi@130.82.238.173:flightcontrol/.
sshpass -p swissless scp flight_control.py pi@130.82.238.173:flightcontrol/.
sshpass -p swissless scp fly.py pi@130.82.238.173:flightcontrol/.
sshpass -p swissless scp startDrone.py pi@130.82.238.173:flightcontrol/.
sshpass -p swissless scp sensor.py pi@130.82.238.173:flightcontrol/.

sshpass -p swissless scp PID.py pi@130.82.237.82:flightcontrol/.
sshpass -p swissless scp ultrasonic_sensor.py pi@130.82.237.82:flightcontrol/.
sshpass -p swissless scp flight_control.py pi@130.82.237.82:flightcontrol/.
sshpass -p swissless scp fly.py pi@130.82.237.82:flightcontrol/.
sshpass -p swissless scp startDrone.py pi@130.82.237.82:flightcontrol/.
sshpass -p swissless scp sensor.py pi@130.82.237.82:flightcontrol/.


sshpass -p swissless scp pi@130.82.238.173:flightcontrol/flight_data.pkl1 .
sshpass -p swissless scp pi@130.82.238.173:flightcontrol/flight_data.pkl2 .
sshpass -p swissless scp pi@130.82.238.173:flightcontrol/flight_data.pkl3 .