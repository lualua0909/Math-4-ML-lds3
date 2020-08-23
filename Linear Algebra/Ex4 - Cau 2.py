# -*- coding: utf-8 -*-
"""============================================================================
   Ex4: MATRICES & VECTORS - Câu 2
       a) Tạo 1 array points có 1000 phần tử cách đều nhau với:
           start = -5, end = 5, step = 0.01
       b) Tạo ma trận điểm có 1000 điểm với x,y = points, point bằng np.meshgrid
       c) Tính z = sqrt(power(x, 2) + power(y, 2))
       d) Biểu diễn z
============================================================================"""
import numpy as np
import matplotlib.pyplot as plt

## a)
points = np.arange(-5, 5, 0.01)
points[:20]

## b)
x, y = np.meshgrid(points, points)
x[:10]
y[:10]

## c)
z = np.sqrt(x ** 2 + y ** 2)

## d)
plt.figure(figsize = (8, 8))
plt.imshow(z, cmap = plt.cm.Blues)
plt.colorbar()
plt.title("Image plot of $\\sqrt{x^2 + y^2}$ for a grid of values")
