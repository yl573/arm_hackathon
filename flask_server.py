from flask import Flask, request
import socket
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
	raw_readings = request.data.decode()
	readings_arr = raw_readings.split('\n')[:-1]

	for i, reading in enumerate(readings_arr):
		readings_arr[i] = reading.split(' ')
	float_readings = np.array(readings_arr).astype(np.float)

	print(float_readings)
	return 'ok'

if __name__ == '__main__':
	print("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
	app.run(host='0.0.0.0', port=8080)