# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:05:17 2020

@author: Maria Sol Vidal
"""
# rotational hamming window (plus radial filter)
import numpy as np
from scipy import interpolate
def rot_hamming(mapp):
    nbins=mapp.shape[0]
    nh=int(nbins/2)
    hamm=np.hamming(nbins)    
    xh, yh = np.meshgrid(np.arange(-nh, nh+1),np.arange(-nh, nh+1))
    r = np.sqrt(xh**2 + yh**2)
    rothamm = np.zeros(r.shape)
    rothamm[r<=nh] = interpolate.interp1d(np.linspace(-nh,nh,nbins),hamm)(r[r<=nh]) 
    return rothamm


# def rot_hamming(mapp):
#     nbins=mapp.shape[0]
#     nh=int(nbins/2)
#     hamm=np.hamming(nbins)    
#     if np.mod(nbins,2)==1:
#         xh, yh = np.meshgrid(np.arange(-nh, nh+1),np.arange(-nh, nh+1))
#         r = np.sqrt(xh**2 + yh**2)
#         rothamm = np.zeros(r.shape)
#         rothamm[r<=nh] = interpolate.interp1d(np.linspace(-nh,nh,nbins),hamm)(r[r<=nh]) 
#     else:
#         xh, yh = np.meshgrid(np.arange(-nh+.5, nh+.5),np.arange(-nh+.5, nh+.5))
#         r = np.sqrt(xh**2 + yh**2)
#         rothamm = np.zeros(r.shape)
#         rothamm[r<=nh] = interpolate.interp1d(np.linspace(-nh+.5, nh-.5,nbins),hamm, bounds_error=False)(r[r<=nh])         
#     return rothamm

