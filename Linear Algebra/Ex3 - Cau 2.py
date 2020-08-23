# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 2
       a) Viết hàm cho phép người dùng nhập vào 1 ma trận A[mxn].
       b) Viết hàm cho phép người dùng nhập vào 1 vector v[n].
       c) Thực hiện phép nhân ma trận với vector trên.
============================================================================="""

import numpy as np

##------------------------------------------------------------------------------
## Hàm nhập các giá trị của ma trận A(m, n) từ bàn phím
##------------------------------------------------------------------------------
def create_matrix(m, n):
    mtr = []
    for i in range(m):
        row = []
        for j in range(n):
            s = "Nhập giá trị A[" + str(i + 1) + ", " + str(j + 1) + "] = "
            a = eval(input(s))
            
            # Thêm giá trị vào dòng hiện hành 
            row.append(a)
            
        # Thêm dòng vào ma trận    
        mtr.append(row)
        
    return np.array(mtr)
##------------------------------------------------------------------------------

##------------------------------------------------------------------------------
## Hàm nhập các giá trị của vector v từ bàn phím
##------------------------------------------------------------------------------    
def create_vector(n):
    v = []
    for i in range(n):
        s = "Nhập giá trị v[" + str(i + 1) + "] = "
        x = eval(input(s))
        
        # Thêm giá trị vào vector
        v.append(x)
        
    return np.array(v)
##------------------------------------------------------------------------------


## Số dòng m và số cột n
m = eval(input("Số dòng m = "))
n = eval(input("Số cột  n = "))
    
## Tạo ma trận A
A = create_matrix(m, n)
print('A =\n', A)

## Tạo vector v
v = create_vector(n)
print('v = ', v)

## Tích
print('A.v = ', A.dot(v))

