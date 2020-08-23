# -*- coding: utf-8 -*-
"""=============================================================================
   Ex3: VECTORS, NATRIX, SCALAR - Câu 4
       a) Tạo ma trận X(mxn) có giá trị trong khoảng 0-11.
       b) Tìm ma trận chuyển vị của X.
       c) Tính X_T.X.
============================================================================="""

import numpy  as np

## Số dòng m và số cột n
m = eval(input("Số dòng m = "))
n = eval(input("Số cột  n = "))
    
## Tạo ma trận X
X = np.arange(12).reshape((m, n))
print('X =\n', X)

## Chuyển vị
print('X.T =\n', X.transpose())
print('X.T =\n', X.T)

## Tích X_T.X
print('X_T.X = ', (X.T).dot(X))

