# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:26:05 2017

@author: sunri
"""
import numpy as np

def getKey(item):
    return item[1]

def detection(yf_plt,N=40,Ts=1.0/40.0,cutoff=2.5,threshold=5.0):
    det=False
    
    xf = np.linspace(0.0, 1.0/(2.0*Ts), int(N/2)) #generate list of frequencies
    
    cutoff_idx = (np.abs(xf-cutoff)).argmin() #find nearest idx in x at cutoff
    
    xy_list = [(xf[i],yf_plt[i]) for i in range(int(N/2))[cutoff_idx:]]
    xy_sorted=sorted(xy_list,key=getKey,reverse=True)
    
    if xy_sorted[0][0]>threshold:
        det=True
    
    return det
    

    

    
    
    
    
    

    
    
yf_plt=np.array([  6.21724894e-16,   4.78946237e-03,   9.76141397e-03,   1.51231765e-02,
   2.11394844e-02,   2.81850741e-02,   3.68430019e-02,   4.81126918e-02,
   6.39137117e-02,   8.85419660e-02,   1.34173956e-01,   2.55007331e-01,
   1.92950500e+00,   3.36068842e-01,   1.44212397e-01,   8.15002817e-02,
   4.44537253e-02,   1.22029886e-02,   2.92282164e-02,   1.17099491e-01,
   8.39041455e-01,   3.58970424e-01,   1.81423688e-01,   1.31392506e-01,
   1.07144802e-01,   9.25915017e-02,   8.27984179e-02,   7.57323115e-02,
   7.03955608e-02,   6.62382398e-02,   6.29309551e-02,   6.02638599e-02,
   5.80968788e-02,   5.63331479e-02,   5.49039316e-02,   5.37596195e-02,
   5.28641407e-02,   5.21913993e-02,   5.17229631e-02,   5.14465705e-02])

a=detection(yf_plt,80)
print(a)