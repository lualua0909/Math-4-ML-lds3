# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 7
       a) Tạo ma trận vuông A(mxm) với các giá trị ngẫu nhiên từ 1 đến 6.
       b) Tạo 1 vector B[n] với giá trị ngẫu nhiên từ 1 đến 3. 
       c) Giải hệ phương trình Ax = B.
============================================================================="""

import numpy  as np
import random

from numpy.linalg import inv

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

##------------------------------------------------------------------------------
## Hàm tạo 1 vector v[n] với giá trị ngẫu nhiên thuộc [start, end]
##------------------------------------------------------------------------------    
def create_vector_random(n, start, end):
    v = []
    for i in range(n):
        x = random.randint(start, end + 1)
        
        # Thêm giá trị vào vector
        v.append(x)
        
    return np.array(v)
##------------------------------------------------------------------------------
    
## Số cấp n của ma trận
n = eval(input("Số cấp n = "))
    
## a) Tạo ma trận vuông A
A = create_matrix_random(n, n, 1, 6)
print('A =\n', A)

## b) Tạo vector B
B = create_vector_random(n, 1, 3)
print('B =', B)

## c) Giải hệ phương trình Ax = B
print('x =', inv(A).dot(B))
print('x =', np.linalg.solve(A,B))

