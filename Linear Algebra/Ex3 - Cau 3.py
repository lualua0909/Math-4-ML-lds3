# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 3
       a) Viết hàm tạo 1 ma trận A[mxn] với giá trị ngẫu nhiên.
       b) Viết hàm tạo 1 vector v[n] với giá trị ngẫu nhiên.
       c) Thực hiện phép nhân ma trận với vector trên.
============================================================================="""

import numpy  as np
import random

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


## Số dòng m và số cột n
m = eval(input("Số dòng m = "))
n = eval(input("Số cột  n = "))
    
## Tạo ma trận A
A = create_matrix_random(m, n, 1, 10)
print('A =\n', A)

## Tạo vector v
v = create_vector_random(n, 5, 15)
print('v = ', v)

## Tích
print('A.v = ', A.dot(v))

