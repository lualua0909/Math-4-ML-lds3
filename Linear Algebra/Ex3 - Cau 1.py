# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 1
       Viết hàm cal_scalar_mult(v, b) với:
           v là vector hoặc ma trận (numpy array)
           b là scalar.
       Hãy thực hiện việc tính toán theo vector/ma trận/scalar được truyền vào.
============================================================================="""

import numpy as np

##------------------------------------------------------------------------------
## Hàm thực hiện các phép toán
##------------------------------------------------------------------------------
def cal_scalar_mult(v, b):
    return v * b
##------------------------------------------------------------------------------
    
## Ma trận
A = np.matrix([[4, 5, 2], [5, 1, 6]])
print('A =\n', A)
print('A * 5 =\n', cal_scalar_mult(A, 5))

## Vector
v = np.array([1, 7, 3, 5, 2, 4])
print('v * 5 =', cal_scalar_mult(v, 5))