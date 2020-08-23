# -*- coding: utf-8 -*-
"""=============================================================================
   Ex2: MATRICES - Câu 1
       Viết hàm cal_matrices(op, m1, m2) với:
           op là một trong các toán tử +, -, *, /
           u và v là 2 ma trận (numpy array) 
       Thực hiện việc tính toán theo các toán tử với hai ma trận được truyền vào.
============================================================================="""

import numpy as np

##------------------------------------------------------------------------------
## Hàm thực hiện các phép toán trên các ma trận
##------------------------------------------------------------------------------
def cal_matrices(op, m1, m2):
    if op == "+":
        result = m1 + m2
    elif op == "-":
        result = m1 - m2
    elif op == "*":
        result = m1 * m2
    elif op == "/":
        result = m1 / m2
    else:
        result = None
    return result
##------------------------------------------------------------------------------
    
m1 = np.array([[1, 3, 2, 4], [4, 3, 6, 8], [5, 6, 3, 1]])
print('M1     =\n', m1)

m2 = np.array([[2, 4, 5, 1], [5, 1, 2, 3], [1, 8, 1, 9]])
print('M2     =\n', m2)

## Phép +
print('M1 + M2 =\n', cal_matrices("+", m1, m2))

## Phép -
print('M1 - M2 =\n', cal_matrices("-", m1, m2))

## Phép *
print('M1 * M2 =\n', cal_matrices("*", m1, m2))

## Phép /
print('M1 / M2 =\n', cal_matrices("/", m1, m2))


