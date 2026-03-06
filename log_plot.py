import matplotlib.pyplot as plt
import pandas as pd

FILENAME = "data_log.csv"

# load csv 
data_frame = pd.read_csv(FILENAME)

# convert time from ms to s
data_frame['time (s)'] = data_frame['time (ms)'] / 1000

# Plot voltage, temp and humidity on the same figure
plt.figure(figsize=(10,6))

plt.plot(data_frame['time (s)'], data_frame['voltage (v)'], label='Voltage (V)', color='blue')
plt.plot(data_frame['time (s)'], data_frame['temperature (C)'], label='Temperature (C)', color='red')
plt.plot(data_frame['time (s)'], data_frame['humidity (%)'], label='Humidity (%)', color='yellow')

plt.xlabel('Time (s)')
plt.ylabel('Sensor Values')
plt.title('ESP32 Data Aquisition system')
plt.legend()
plt.grid(True)
plt.show()