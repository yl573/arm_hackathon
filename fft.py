# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:26:37 2017

@author: sunri
"""
import numpy as np
import random
import matplotlib.pyplot as plt

#y = x + 2*random.randrange(10);


def fft(y,N=80,Ts=1.0/40.0):

    
    from scipy.fftpack import fft
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*Ts), int(N/2))
    yf_plt = 2.0/N * np.abs(yf[0:int(N/2)])
    inte=np.sum(yf_plt[16:])

    '''
    from scipy.integrate import simps
    inte = simps(yf_plt,xf)
    print(inte)
    '''
    return xf,yf_plt,inte


# Number of samplepoints
N = 80
# sample spacing
Ts = 1.0 / 40.0
t = np.linspace(0.0, N*Ts, N)
y1 = 2*np.sin(6 * 2.0*np.pi*t) + 1*np.sin(10 * 2.0*np.pi*t)
r = [random.randrange(1000)/1000 for i in y1]
y = y1 #+ r
y2 = [np.sin(6 * 2.0*np.pi*i) + 0.5*np.sin(10 * 2.0*np.pi*i) for i in t[40:]]
y = [0]*40+y2
xf, yf_plt, inte = fft(y)


print(inte)
plt.plot(t, y)
plt.grid()
plt.show()

plt.plot(xf, yf_plt)
plt.grid()
plt.show()

'''
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

Fs = 40.0;  # sampling rate
T = 2
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,T,Ts) # time vector

y1 = np.sin(10 * 2.0*np.pi*t) + 0.5*np.sin(15 * 2.0*np.pi*t)
y = y1#[i+random.randrange(10)/10 for i in y1]

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range

Y = 2*np.fft.fft(y)/n # fft computing and normalization
print(Y)
Y = Y[range(int(n/2))]


plt.plot(t,y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

plt.plot(frq,abs(Y),'r') # plotting the spectrum
plt.xlabel('Freq (Hz)')
plt.ylabel('|Y(freq)|')
plt.grid()
plt.show

'''
