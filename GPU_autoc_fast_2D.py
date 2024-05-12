# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 07:57:13 2021

@author: Maria Sol Vidal
"""

import tensorflow as tf
def autoc_fast_2D(mapp): # cambiar por otra funcion 
    myone=tf.ones(mapp.shape)
    myone_i=tf.constant(tf.reshape(myone, (1, myone.shape[0],myone.shape[1] , 1)))
    myone_k=tf.constant(tf.reshape(myone, ( myone.shape[0],myone.shape[1] ,1, 1)))
    mapp_i=tf.constant(tf.reshape(mapp, (1, myone.shape[0],myone.shape[1] , 1)))
    mapp_k=tf.constant(tf.reshape(mapp, ( myone.shape[0],myone.shape[1] ,1, 1)))
    dim=myone.shape[0]-1
    nn=tf.nn.conv2d(myone_i, myone_k, strides=[1, 1], padding=[[0, 0], [dim,dim], [dim, dim], [0, 0]])[0, ..., 0]
    mx=tf.nn.conv2d(mapp_i, myone_k, strides=[1, 1], padding=[[0, 0], [dim,dim], [dim, dim], [0, 0]])[0, ..., 0]/nn
    my=tf.nn.conv2d(myone_i, mapp_k, strides=[1, 1], padding=[[0, 0], [dim,dim], [dim, dim], [0, 0]])[0, ..., 0]/nn
    auto=tf.nn.conv2d(mapp_i, mapp_k, strides=[1, 1], padding=[[0, 0], [dim,dim], [dim, dim], [0, 0]])[0, ..., 0]/nn-mx*my
    auto=auto/((((tf.nn.conv2d(tf.constant(tf.reshape(mapp**2, (1, myone.shape[0],myone.shape[1] , 1))), myone_k, strides=[1, 1], padding=[[0, 0], [dim,dim], [dim, dim], [0, 0]])[0, ..., 0])/nn-mx*mx)*((tf.nn.conv2d(myone_i,tf.constant(tf.reshape(mapp**2, ( myone.shape[0],myone.shape[1] , 1,1))), strides=[1, 1], padding=[[0, 0], [dim,dim], [dim, dim], [0, 0]])[0, ..., 0])/nn-my*my))**0.5)
    return auto













