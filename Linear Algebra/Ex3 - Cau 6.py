# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 6
       a) Tạo ma trận vuông A(mxm) với các giá trị ngẫu nhiên từ 5 đến 10.
       b) Tính tổng các phần tử trên đường chéo chính (trace). 
       c) Tính định thức của A.
       d) Tính hạng của A.
============================================================================="""

import numpy  as np
import random

from numpy.linalg import det, matrix_rank

##------------------------------------------------------------------------------
## Hàm tạo 1 ma trận A[mxn] với giá trị ngẫu nhiên thuộc [start, end]
##------------------------------------------------------------------------------
def create_matrix_random(m, n, start, end):
    mtr = []
    for i in range(m):
        row = []
        for j in range(n):
            a = random.randint(start, end + 1)
            
            # Thêm giá trị vào dòng hiện hành 
            row.append(a)
            
        # Thêm dòng vào ma trận    
        mtr.append(row)
        
    return np.array(mtr)
##------------------------------------------------------------------------------

## Số cấp n của ma trận
n = eval(input("Số cấp n = "))
    
## Tạo ma trận vuông A
A = create_matrix_random(n, n, 5, 10)
print('A =\n', A)

## b) 
print('trace(A) =', np.trace(A))

## c)
print('|A| =', det(A))

## d)
print('rank(A) =', matrix_rank(A))

