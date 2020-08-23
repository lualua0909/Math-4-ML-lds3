# -*- coding: utf-8 -*-
"""=============================================================================
   Ex1: VECTORS - Câu 1
       Viết hàm cal_vectors(op, u, v) với:
           op là một trong các toán tử +, -, *, /, "dot"
           u và v là 2 vectors (numpy array) 
       Thực hiện việc tính toán theo các toán tử với hai vectors được truyền vào.
============================================================================="""

import numpy as np

##------------------------------------------------------------------------------
## Hàm thực hiện các phép toán trên các vectors
##------------------------------------------------------------------------------
def cal_vectors(op, u, v):
    if op == "+":
        result = u + v
    elif op == "-":
        result = u - v
    elif op == "*":
        result = u * v
    elif op == "/":
        result = u / v
    elif op == "dot":
        result = u.dot(v)
    else:
        result = None
    return result
##------------------------------------------------------------------------------
    
u = np.array([1, 3, 4, 6, 3, 4, 5])
print('u     =', u)

v = np.array([4, 7, 1, 2, 3, 8, 9])
print('v     =', v)

## Phép +
print('u + v =', cal_vectors("+", u, v))

## Phép -
print('u - v =', cal_vectors("-", u, v))

## Phép *
print('u * v =', cal_vectors("*", u, v))

## Phép /
print('u / v =', cal_vectors("/", u, v))

## Phép tích vô hướng
print('u.v   = ', cal_vectors("dot", u, v))
