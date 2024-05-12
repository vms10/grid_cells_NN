# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:43:14 2020

@author: Maria Sol Vidal
"""
import numpy as np
def corr(J, A): # J y A tienen que tener el mismo numero de filas
    cols=A.shape[1]
    filas=J.shape[1]
    return np.corrcoef(J, A,rowvar=False)[:filas,-cols:]
