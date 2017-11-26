# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:26:37 2017

@author: sunri
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.fftpack import fft

#y = x + 2*random.randrange(10);

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

def fft_transform(y,N=40,Ts=1.0/40.0,cutoff=8):
    
    y_mag=np.array([np.linalg.norm(i) for i in y])
    

    yf = fft(y_mag)
    xf = np.linspace(0.0, 1.0/(2.0*Ts), int(N/2))
    yf_plt = 2.0/N * np.abs(yf[0:int(N/2)])
    
    idx = find_nearest(xf,8)
    inte=np.sum(yf_plt[idx:])

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
y1 = 2*np.sin( 6* 2.0*np.pi*t) + 1*np.sin(10 * 2.0*np.pi*t)
y = [[i ,0,0] for i in y1]
#+ random.randrange(1000)/1000
#y2 = [np.sin(6 * 2.0*np.pi*i) + 0.5*np.sin(10 * 2.0*np.pi*i) for i in t[40:]]
#y = [0]*40+y2
xf, yf_plt, inte = fft_transform(y,N,Ts,8)

print(inte)

plt.plot(xf, yf_plt)
plt.grid()
plt.show()


