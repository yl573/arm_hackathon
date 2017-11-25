from flask import Flask, request
import socket
import numpy as np
import fft
import matplotlib.pyplot as plt
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
	raw_readings = request.data.decode()
	readings_arr = raw_readings.split('\n')[:-1]

	for i, reading in enumerate(readings_arr):
		readings_arr[i] = reading.split(' ')
	float_readings = np.array(readings_arr).astype(np.float)

	N = 40
	Ts = 1.0/40
	(xf,yf_plt,inte) = fft.fft_transform(float_readings,N=N,Ts=Ts)

	
	plt.xlabel('Frequency')
	plt.ylabel('Power')
	plt.ylim(0,1)
	plt.plot(xf[2:], yf_plt[2:])
	plt.pause(0.2)
	plt.clf()
	#plt.show(block=False)


	print(yf_plt)
	return 'ok'

if __name__ == '__main__':
	print("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
	app.run(host='0.0.0.0', port=8080)