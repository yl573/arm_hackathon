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



def fft_transform(y,N=40,Ts=1.0/40.0,cutoff=8):
    
    # NOTE: X_T is in the form [[x1,x2,...,xn],[y1,y2,...,yn],[z1,z2,...,zn]], 
    # otherwise is in the form [[x1,y1,z1],[x2,y2,z2],......,[xn,yn,zn]].
    y_T = np.transpose(np.array(y))
    
    yf_T = [fft(y_T[0]),fft(y_T[1]),fft(y_T[2])]
    yf = np.transpose(np.array(yf_T))
    
    yf_mag = [np.linalg.norm(i) for i in yf]
    
    xf = np.linspace(0.0, 1.0/(2.0*Ts), int(N/2))
    yf_plt = 2.0/N * np.abs(yf_mag[0:int(N/2)])
    
    idx = (np.abs(xf-cutoff)).argmin() #find nearest idx in x at cutoff
    inte = np.sum(yf_plt[idx:])

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

print('integral for freq > cutoff is',inte)

plt.plot(xf, yf_plt)
plt.grid()
plt.show()


