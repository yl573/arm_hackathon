from flask import Flask, request, Response
import socket
import numpy as np
import fft
import matplotlib.pyplot as plt
import time
import threading
import detection
from sms_new import send_sms
from database import save_to_db
from cache import MyCache

check_seconds = 5

global cancel_alarm
global alarm_countdown
global additional
cancel_alarm = False
alarm_countdown = False
additional = ''

cache=MyCache(5)

def alarm():
	global cancel_alarm
	global alarm_countdown
	acc_array = cache.cache['acc']['value'].tolist()
	if additional != '':
		temp, light, hum, co2 = tuple([float(x) for x in additional.split(' ')])
	else:
		temp, light, hum, co2 = (0,0,0,0)
	if not cancel_alarm:
		print('Alarm!!!')
		is_seizure = True
		try:
			send_sms('Seizure Alert!')
		except Exception:
			print('cannot send sms')
	else:
		print('False alarm!!!')
		is_seizure = False

	save_to_db(temp, light, hum, co2, acc_array, True)	
	cancel_alarm = False
	alarm_countdown = False

app = Flask(__name__)

def make_response(msg_str):
	msg = str.encode(msg_str)
	res = Response(msg_str, mimetype="text/plain")
	# res.headers.add('content-Length', len(msg))
	return res

@app.route('/', methods=['POST'])
def on_data():
	global cancel_alarm
	global alarm_countdown
	if not alarm_countdown:
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
		plt.plot(xf, yf_plt)
		plt.pause(0.2)
		plt.clf()

		cache.update('acc',float_readings)

		seizure = detection.detect(yf_plt, threshold=4, amp_thresh=0.6)
		print(seizure)
		if seizure:
			threading.Timer(check_seconds, alarm).start()
			alarm_countdown = True
			return make_response('not ok')
		else:
			return make_response('ok')
	else:
		return make_response('countdown')

@app.route('/cancel', methods=['POST'])
def cancel_timer():
	global cancel_alarm
	cancel_alarm = True
	print('alarm cancelled')
	return make_response('cancelled')

@app.route('/additional', methods=['POST'])
def recieve_light():
	global additional
	raw_readings = request.data.decode()
	additional = raw_readings
	return make_response('recieved')

if __name__ == '__main__':
	print("Your IP address is: %s" % socket.gethostbyname(socket.gethostname()))
	app.run(host='0.0.0.0', port=8080)