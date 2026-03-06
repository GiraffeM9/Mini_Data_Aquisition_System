import serial, csv
from datetime import datetime

# Adjust this to your requirements
SERIAL_PORT = "COM5"
BAUD_RATE = 115200
CSV_FILE = "data_log.csv"
NUM_READINGS = 100 # 100 lines of readings

# open serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# open csv file for writing
file = open(CSV_FILE, 'w')
writer = csv.writer(file)

# write header
header = ["time (ms)", "voltage (v)", "humidity (%)", "temperature (C)", "Heat index (C)"]
writer.writerow(header)

print("Press button to start...")

logging_started = False
count = 0

while count < NUM_READINGS:

    line = ser.readline().decode('utf-8').strip()

    if line:
        data = line.split(",")
        # ignore any messages that is not readings and detect button press to start logging
        if len(data) == 5:
            if not logging_started:
                print("Starting logging...")
                logging_started = True

            writer.writerow(data)
            print(data)
            count += 1

file.close()
ser.close()

print("Finished logging")