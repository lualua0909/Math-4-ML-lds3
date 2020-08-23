# -*- coding: utf-8 -*-
"""=============================================================================
    Ex5: SPARSE MATRIX - Câu 2
        a) Tạo ra một ma trận BigA(1000, 1000) phần tử ngẫu nhiên tử -10 đến 5.
        b) Thay thế giá trị 0 cho tất cả các phần tử âm trong ma trận BigA
        c) Tính kích thước của ma trận BigA
        d) Tạo sparse matrix BigS từ BigA
        e) Tích kích thước của BigS
        f) Tính sparsity của sparse matrix
        g) Trực quan hóa BigS
============================================================================="""

from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import numpy             as np

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
BigA = create_matrix_random(1000, 1000, -10, 5)

## b)
BigA[BigA < 0] = 0

## c) Xem kích thước
print("Size of full matrix with zeros =", BigA.nbytes/(1024**2), " MB") 

## d)
BigS = csr_matrix(BigA)

## e)
print("Size of csr_matrix =", BigS.data.nbytes/(1024**2), " MB")

## f)
plt.figure(figsize = (10, 10))
plt.spy(BigS, markersize = 0.1)



