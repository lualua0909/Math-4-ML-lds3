"""=============================================================================
    Ex1: DECOMPOSITION
    Câu 1: LU Decomposition
        a) Tạo ma trận A(4 x 5) chứa các giá trị ngẫu nhiên trong khoảng 1 - 10
        b) Phân tích thành các thành phần P, L, U. In kết quả
        c) Tái tạo lại ma trận A từ các thành phần P, L, U
============================================================================="""
    
import numpy  as np
import random       
from scipy.linalg import lu

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

## a) Tạo ma trận A(4 x 5) chứa các giá trị ngẫu nhiên trong khoảng 1 - 10
## Ma trận HÌNH CHỮ NHẬT: A(m, n) = P_T(m, m).L(m, n).U(n, n)
m, n, min, max = 5, 4, 1, 10
A = create_matrix_random(m, n, min, max)
print('Ma trận A', A.shape, ':\n', A)

## b) Phân tích thành các thành phần P, L, U. In kết quả
P_T, L, U = lu(A)

print('Ma trận P_T', P_T.shape, ':\n', P_T)
print('Ma trận L', L.shape, ':\n', L)
print('Ma trận U', U.shape, ':\n', U)

## c) Tái tạo lại ma trận B từ các thành phần P, L, U
print('Tái tạo ma trận A:\n', P_T.dot(L).dot(U))
