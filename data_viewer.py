import matplotlib
print matplotlib.__version__

import matplotlib.pyplot as plt

with open('flight_data.pkl', 'rb') as f:
    time_list, setpoint_list, feedback_list, pidout_list = pickle.load(f)

plt.plot(
    time_list, setpoint_list, 'b', 
    time_list, feedback_list, 'r')

plt.plot(time_list, pidout_list)
plt.show()