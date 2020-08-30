"""=============================================================================
    Ex2: EIGENDECOMPOSITION
    Câu 2:
        a) Tạo ma trận A(4 x 4) chứa các giá trị ngẫu nhiên trong khoảng 1 - 9
        b) Tạo ma trận đối xứng B = A.A_T
        c) Phân tích eigenvalues và eigenvectors của B
============================================================================="""

import numpy as np
from numpy.linalg import eig

## a) Tạo ma trận A(5 x 5) chứa các giá trị ngẫu nhiên trong khoảng 1 - 10
m, n, min, max = 4, 4, 1, 9
A = np.random.randint(1, 10, (n, n))
print('Ma trận A', A.shape, ':\n', A)

## b) Tạo ma trận đối xứng B = A.A_T
B = A @ A.T
print('Ma trận đối xứng B', B.shape, ':\n', B)

## c) Phân tích eigenvalues và eigenvectors
values, vectors = eig(B)

print('Eigenvalues',  values.shape,  ':\n', values)
print('Eigenvectors', vectors.shape, ':\n', vectors)

