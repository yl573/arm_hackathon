# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:26:37 2017

@author: sunri
"""
import numpy as np
import random
import matplotlib.pyplot as plt

#y = x + 2*random.randrange(10);



def fft_transform(y,N=40,Ts=1.0/40.0,cutoff=8):
    
    
    from scipy.fftpack import fft
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*Ts), int(N/2))
    yf_plt = 2.0/N * np.abs(yf[0:int(N/2)])
    
    idx = (np.abs(xf-cutoff)).argmin() #find nearest idx in x at cutoff
    inte1=np.sum(yf_plt[idx:])

    print(yf_plt)
    from scipy.integrate import simps
    inte2 = simps(yf_plt[idx:],xf[idx:])
    
    print(yf_plt[idx])

    return xf,yf_plt,inte1,inte2


# Number of samplepoints
N = 80
# sample spacing
Ts = 1.0 / 40.0
t = np.linspace(0.0, N*Ts, N)
y1 = 2*np.sin( 6* 2.0*np.pi*t) + 1*np.sin(10 * 2.0*np.pi*t)
y = y1
#+ random.randrange(1000)/1000
#y2 = [np.sin(6 * 2.0*np.pi*i) + 0.5*np.sin(10 * 2.0*np.pi*i) for i in t[40:]]
#y = [0]*40+y2
xf, yf_plt, inte1,inte2 = fft_transform(y,N)


print(inte1,inte2)
plt.plot(t, y)
plt.grid()
plt.show()

plt.plot(xf, yf_plt)
plt.grid()
plt.show()


