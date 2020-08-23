# -*- coding: utf-8 -*-
"""=============================================================================
   Ex1: VECTOR NORMS - Câu 2
       Viết hàm cal_vector_norm(t, v) với:
           t là một trong các loại L1, L2, Max
           v là vector.
============================================================================="""

import math
import numpy as np

from numpy.linalg import norm

##------------------------------------------------------------------------------
## Hàm tính chuẩn của vector
##------------------------------------------------------------------------------
def cal_vector_norm(t, v):
    t = t.upper()
    if t == "L1":
        result = norm(v,1)
    elif t == "L2":
        result = norm(v)
    elif t == "MAX":
        result = norm(v, math.inf)
    else:
        result = None
    return result

##------------------------------------------------------------------------------
    
v = np.array([1, 3, -4, 5, 7, 9, -6])
print('v       =', v)

## L1
print('L1(v)   =', cal_vector_norm("L1", v))

## L2
print('L2(v)   =', cal_vector_norm("L2", v))

## Lmax
print('Lmax(v) =', cal_vector_norm("Max", v))

