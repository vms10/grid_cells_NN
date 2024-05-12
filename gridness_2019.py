# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:54:35 2020

@author: Maria Sol Vidal
"""
import numpy as np
from scipy import interpolate, ndimage
from skimage import filters
def gridness_2019(autoc, abins,rot_hamming,rx,ry,angbins,b,tbins):
    autoc[np.isnan(autoc)]=0
    autoc[np.isinf(autoc)]=0
    autocr=autoc*rot_hamming
    f=interpolate.interp2d(abins,abins,autocr)
    aux3=(interpolate.dfitpack.bispeu(f.tck[0], f.tck[1], f.tck[2], f.tck[3], f.tck[4], rx.ravel(), ry.ravel())[0]).reshape(rx.shape)
    m3spac= (aux3*b).mean(0)
    i = np.nanargmax(np.abs(m3spac)) #el indice que maximiza
    imax=np.mod(np.arange(1,len(angbins),40)-round(np.angle(m3spac[i])/6/np.pi*120)-1,len(angbins))
    imin=np.mod(np.arange(21,len(angbins),40)-round(np.angle(m3spac[i])/6/np.pi*120)-1,len(angbins))
    myaux=aux3[:,max(0,i-9):min(i+9,len(abins))]
    img=filters.gaussian(np.tile(myaux, (3, 1)), sigma=5,mode = 'nearest',truncate=2.0)
    lm = ndimage.filters.maximum_filter( img,size=8 )
    BW = (img == lm) #// convert local max values to binary mask #avoid maxima at edges
    BW = BW[len(angbins):2*len(angbins),:]
    findx=np.where(BW!=0)
    sindx=(-myaux[findx]).argsort(axis=0)
    findx=np.ravel_multi_index(findx, BW.shape, mode='raise', order='F')
    fsel=np.arange(0,min(3,len(sindx)))
    sindx=sindx[fsel]
    A,R = np.unravel_index(findx[sindx], BW.shape, order='F')
    R_=i-10+R
    #R_=i-9+R asi da igual que matlab 
    A_=angbins[A]
    X=np.empty(3)
    X[:]=np.nan
    Y=np.empty(3)
    Y[:]=np.nan
    V=np.empty(3)
    V[:]=np.nan
    X[fsel]=-R_*np.cos(A_)# no da igual por lo indices 
    Y[fsel]=R_*np.sin(A_) # noda igual por los indices 
    V[fsel]=myaux[A, R]
    return ((aux3[imax,i]-aux3[imin,i]).mean(0)), tbins[i], np.concatenate((X, -X)), np.concatenate((Y, -Y)), np.concatenate((V, V)), autocr.ravel(order="F")