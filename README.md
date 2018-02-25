
# Motivation

Whoop whoop whoop -a nuclear plant is suffering a blackout, Rolls Royces' power engines kicked in to keep the fuel rods at safe cool temperatures. Suddenly one of the engines fails, it sets on fire!

To prevent a fallout from happening, you have 36 hours to program a drone (with a Raspberry Pi core) that:
- takes off when the start-light switches from red to green.
- autonmomously flies through the plant.
- identifies the buring engine and sends out a picture of it.
- lands safely on the starting pad.

That was Rolls Royces' challenge to us during the StartHack 2018 hackathon in St. Gallen, 23-25 February 2018.

# Achievements

Although we wouldn't have saved the world if this was a real emergency, we are happy with what we hacked together over these past hours.
![Drone](https://github.com/ckauth/swissless/blob/master/illustrations/drone.png)

Once the start-light switches green, our drone sets out to fly through the tents to screen the engines. The flight style is like Manhattan in 3D, and PID regulators stabilize the trajectory. Although we had neat ideas on how to implement more fluid trajectories, we finally settled for simplicity. The Manhattan flight style has the huge advantage that each direction of flight needs only one ultrasonic sensor to measure the distance to the next obstacle, on which the PID regulates.

![InAction](https://github.com/ckauth/swissless/blob/master/illustrations/inAction.png)

By the time of the final competition, all propellers (of the single available drone) had been broken - take it as a sign of motivation and persistence of all teams -, and the drone had to be carried through the space by following the direction that the propeller engines whistled.

![Panorama](https://github.com/ckauth/swissless/blob/master/illustrations/panorama.png)

Once arrived in the engine tent, the drone rotates around its axis and takes pictures. Those pictures are uploaded to a server and concatenated into a panorama. This makes it particularly simple to identify the burning engine from the average green and red channels of the RGB image.

# User Guide

The code is as structured as a hackathon permits it to be ;) You may start your exploration in the _fly.py_ file.
