"""=============================================================================
    Ex3: SVD
    Câu 3: 
        a) Tạo ma trận A(4 x 6) chứa các giá trị ngẫu nhiên trong khoảng 1 - 10
        b) Tạo ma trận giả nghịch đảo của A
============================================================================="""
    
import numpy as np
from scipy.linalg import pinv

## a) Tạo ma trận A(4 x 6) chứa các giá trị ngẫu nhiên trong khoảng 1 - 10
A = np.array([[4, 0], [3, -5]])
A = np.random.randint(1, 11, (4, 6))
print('Ma trận A', A.shape, ':\n', A)

## b) Tạo ma trận giả nghịch đảo của A
print('***** Cách 1: Dùng hàm scipy.linalg.pinv() *****')
B = pinv(A)
print('Ma trận giả nghịch đảo B', B.shape, 'của A:\n', B)
print('Kiểm chứng A @ B = I(m)', (A @ B).shape, ':\n', A @ B)
print('Kiểm chứng B @ A = I(n)', (B @ A).shape, ':\n', B @ A)

print('\n***** Cách 2: Dùng công thức tính toán *****')
## Phân rã SVD
U, s, VT = np.linalg.svd(A)
print('         - Ma trận U',   U.shape, ':\n', U)
print('         - Eigenvalues:', s, '\n')
print('         - Ma trận V.T', VT.shape, ':\n', VT)

## Nghịch đảo của ma trận đường chéo S
S_1 = np.zeros(A.T.shape)
d   = 1.0 / s
S_1[:A.shape[0],:A.shape[0]] = np.diag(d)

print('         - Ma trận nghịch đảo của S', S_1.shape, ':\n', S_1)
B = (VT.T) @ S_1 @ U.T

print('Ma trận giả nghịch đảo TRÁI B', B.shape, 'của A:\n', B)
print('Kiểm chứng A @ B = I(m)', (A @ B).shape, ':\n', A @ B)
print('Kiểm chứng B @ A = I(n)', (B @ A).shape, ':\n', B @ A)
