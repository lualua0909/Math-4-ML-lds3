#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Hàm tính m (slope), b (theta/bias):    y = mx + b
def gradient_descent_2(alpha, x, y, numIterations):
    M     = x.shape[0] # number of samples
    theta = np.ones(2)
    x_T   = x.transpose()
    for iter in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss       = hypothesis - y
        # J          = np.sum(loss ** 2) / (2 * M)  # cost
        # print("iter %s | J: %.3f" % (iter, J))      
        gradient   = np.dot(x_T, loss) / M      
        
        theta    = theta - (alpha * gradient)  # update
    return theta



