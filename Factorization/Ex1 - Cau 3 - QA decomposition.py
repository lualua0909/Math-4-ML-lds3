"""=============================================================================
    Ex1: DECOMPOSITION
    Câu 3: QA Decomposition
        a) Tạo ma trận A(4 x 4) chứa các giá trị ngẫu nhiên trong khoảng 5 - 10
        b) Phân tích thành các thành phần Q và R. In kết quả
        c) Tái tạo lại ma trận A từ các thành phần Q và R
============================================================================="""
    
import numpy  as np
import random       
from scipy.linalg import qr

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

## a) Tạo ma trận A(4 x 4) chứa các giá trị ngẫu nhiên trong khoảng 5 - 10
m, n, min, max = 4, 4, 5, 10
A = create_matrix_random(m, n, min, max)
print('Ma trận A', A.shape, ':\n', A)

## b) Phân tích thành các thành phần Q và R. In kết quả
Q, R = qr(A)

print('Ma trận Q', Q.shape, ':\n', Q)
print('Ma trận R', R.shape, ':\n', R)

## c) Tái tạo lại ma trận A từ các thành phần Q và R
print('Tái tạo ma trận A:\n', Q.dot(R))
