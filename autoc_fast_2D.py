# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:37:36 2020

@author: Maria Sol Vidal
"""
import numpy as np
from scipy import signal
def autoc_fast_2D(mapp): # cambiar por otra funcion 
    myone=np.ones(mapp.shape)
    nn=signal.fftconvolve(myone, np.rot90(myone, k=2))
    mx=signal.fftconvolve(mapp, np.rot90(myone, k=2))/nn
    my=signal.fftconvolve(myone, np.rot90(mapp, k=2))/nn
    auto=signal.fftconvolve(mapp, np.rot90(mapp, k=2))/nn-mx*my
    auto=auto/(np.spacing(1)+np.sqrt((signal.fftconvolve(mapp**2, np.rot90(myone, k=2))/nn-mx*mx)*(signal.fftconvolve(myone, np.rot90(mapp**2, k=2))/nn-my*my)))
    return auto