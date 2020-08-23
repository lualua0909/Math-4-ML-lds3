# -*- coding: utf-8 -*-
"""=============================================================================
    Ex5: SPARSE MATRIX - Câu 1
        a) Tạo ma trận A(5, 5) với các giá trị ngẫu nhiên từ -10 đến 5
        b) Thay thế giá trị 0 cho tất cả các phần tử âm trong ma trận A
        c) Tạo sparse matrix S từ A
        d) Tính sparsity của sparse matrix 
============================================================================="""
    
import numpy as np
from scipy.sparse     import csr_matrix

##------------------------------------------------------------------------------
## Hàm tạo ma trận với các giá trị ngẫu nhiên
##------------------------------------------------------------------------------
def create_matrix_random(m, n, start, end):
    import random as rd
    
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            x = float(rd.randint(start,end+1))
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)
##------------------------------------------------------------------------------

## a)
A = create_matrix_random(5, 5, -10, 5)
print('A =\n', A)

## b)
A[A < 0] = 0
print('A+ =\n', A)

## c)
print('CSR =\n', csr_matrix(A))

## d)
print(1.0 - (np.count_nonzero(A) / A.size) )
