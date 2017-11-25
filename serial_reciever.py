import serial

ser = serial.Serial('/dev/tty.usbmodem1422')  # open serial port
print(ser.name)         # check which port was really used

while True:
    line = ser.readline()
    print(line)
ser.close()             # close port