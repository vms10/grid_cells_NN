# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:47:49 2020

@author: Maria Sol Vidal
"""
import numpy as np
from autoc_fast_2D import autoc_fast_2D
from rot_hamming import rot_hamming
from corr import corr
import matplotlib.pyplot as plt
def plot_all_grid(mapp,gridness,X,Y,V,mngr,mnWJ,W,mnal,gridness_mean,pgr,Wautoc,Jautoc,ffacc,rracc,ms,NmEC,ff,rr,contador):
    i = np.nanargmax(gridness)
    mymapss=np.reshape(mapp[i,:], (ms, ms), order="F")
    auxss=autoc_fast_2D(mymapss)  
    tiempos=np.arange(0,contador+1)*pgr/60 # en minutos        
    plt.figure(figsize=(15,10))
    plt.subplot(331) # 131 1 fila, 3 columnas, primer grafico
    plt.imshow(mymapss, cmap= 'jet')
    plt.colorbar()
    #plt.title('A: ' + (A,2) ' / NIs: ' trunc(NIs,1) ' - ' num2str(rep))
    #plt.xlabel("x", fontsize=15)
    #plt.ylabel("y", fontsize=15, rotation=0, labelpad=20)
    # Repetimos para un segundo gráfico
    plt.subplot(332) # 132 1 fila, 3 columnas, segundo grafico
    plt.imshow(auxss*rot_hamming(auxss), cmap= 'jet',vmin=-.3, vmax=1)
    plt.colorbar()
    plt.title('cell ' + str(i) + ' - ' + str(gridness[i]))
    #plt.xlabel("tiempo", fontsize=15)
    #plt.ylabel("x", rotation=0, fontsize=15)
    
    # Repetimos para un tercer gráfico
    plt.subplot(333) # 133 1 fila, 3 columnas, tercer grafico
    plt.plot(tiempos, mngr[:contador+1] , label='mngr')
    plt.plot(tiempos,gridness_mean[:contador+1], label='gridness mean')
    plt.ylim(0,1)
    plt.legend()
    #plt.xlabel("tiempo", fontsize=15)
    #plt.ylabel("y", rotation=0, fontsize=15)
    plt.subplot(334)
    plt.plot(tiempos, mnWJ[:contador+1] , label='mnWJ') # matriz de conectividad
    plt.plot(tiempos, ffacc[:contador+1] , label='ffacc')
    plt.plot(tiempos, rracc[:contador+1] , label='rracc')
    plt.ylim(0,1)
    plt.legend()
#    plt.subplot(233)
#    V[V<0]=0.0001
#    plt.set_cmap('RdBu')
#    plt.scatter(X.ravel(order='F'), Y.ravel(order='F'), c=50*V.ravel(order='F'))
#    plt.colorbar()
#    plt.scatter(X[:,i], Y[:,i], 'o')    
    plt.subplot(335)
    plt.imshow(Wautoc, cmap= 'jet')
    plt.colorbar()
    plt.subplot(336)
    plt.plot(tiempos, mnal[:contador+1] , label='mnal')
    plt.ylim(0,1)
    plt.legend()
    plt.subplot(337)
    plt.imshow(Jautoc, cmap= 'jet')
    plt.colorbar()
    plt.title('FF: ' + str(ff) +  ' - RR: ' + str(rr))
#    plt.subplot(236)
#    v, i = (corr(mapp,W)).max(axis=1), (corr(mapp,W)).argmax(axis=1)
#    mx, my = np.meshgrid(np.arange(1,ms+1),np.arange(1,ms+1))
#    plt.set_cmap('RdBu')
#    plt.scatter(mx.ravel(order='F'),ms+1-my.ravel(order='F'),c=20*v )
#    plt.title('MS: ' + str(np.half(map_sparseness)))
    plt.tight_layout()
    plt.show()
