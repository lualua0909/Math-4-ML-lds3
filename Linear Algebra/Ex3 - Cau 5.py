# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 5
       a) Tạo ma trận vuông A(mxm) với các giá trị ngẫu nhiên từ 1 đến 4.
       b) Tạo ma trận nghịch đảo của A
       c) Tính A.B
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

## Số cấp n của ma trận
n = eval(input("Số cấp n = "))
    
## Tạo ma trận vuông A
A = create_matrix_random(n, n, 1, 4)
print('A =\n', A)

## Ma trận nghịch đảo
print('A-1 =\n', inv(A))

## Kiểm tra ma trận nghịch đảo
print('A-1.A = ', A.dot(inv(A)))

