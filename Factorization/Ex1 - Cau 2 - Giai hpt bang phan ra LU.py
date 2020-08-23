"""=============================================================================
    Ex1: DECOMPOSITION
    Câu 2: Giải hệ phương trình bằng LU Decomposition
        a) Quy về Ax = B. Sau đó giải tìm x.
        b) Phân tích thành các thành phần P, L, U. In kết quả.
        c) Tái tạo lại ma trận A từ các thành phần P, L, U.
============================================================================="""
import numpy        as np    
import scipy.linalg as linalg

from scipy.linalg import lu

## Câu 2
A = np.array([[2, 1, 1], 
              [1, 3, 2], 
              [1, 0, 0]])
B = np.array([4, 5, 6]) 

## Ví dụ thêm
A = np.array([[10, 8, 10,  8], 
              [ 8, 6,  6, 10], 
              [ 3, 3,  6,  3],
              [11, 8,  6,  1]])
B = np.array([4, 5, 6, 7]) 

print('Ma trận A', A.shape, ':\n', A)

print('************************ Hàm scipy.linalg.lu() ***********************\n')
P_T, L, U = lu(A)

print('Ma trận P_T', P_T.shape, ':\n', P_T)
print('Ma trận L', L.shape, ':\n', L)
print('Ma trận U', U.shape, ':\n', U)


print('********************* Hàm scipy.linalg.lu_factor() *******************\n')
## Giải hệ phương trình
## //docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.linalg.lu_factor.html
##    Hàm lu_factor(A) trả về 2 đối tượng:
##       - Ma trận nxn: U + (L - diag(L))
##       - Mảng [n] chứa các chỉ số dòng của I(n) để tạo nên P
##------------------------------------------------------------------------------
## Hàm tạo ma trận hoán vị P từ pivot = linalg.lu_factor(A)[1]
def permutationMatrix(pivot):
    # Khởi tạo P bằng ma trận đơn vị
    P = np.identity(len(pivot))

    # i: index; r: element
    for i, r in enumerate(pivot):
        # pivot[i] = r
        # Hoán đổi dòng r và dòng pivot[i] của ma trận I
    
        I = np.identity(len(pivot))
    
        temp    = I[i, :].copy()
        I[i, :] = I[r, :]
        I[r, :] = temp 
        
        P = P.dot(I)
    return P
##------------------------------------------------------------------------------

LU = linalg.lu_factor(A)

print('Ma trận kết hợp U + L - diag(L)', LU[0].shape, ':\n', LU[0])

U = np.triu(LU[0])
L = LU[0] - U + np.identity(len(B))

print('Ma trận L', L.shape, ':\n', L)
print('Ma trận U', U.shape, ':\n', U)

## Ma trận hoán vị
print('Mảng pivot', LU[1].shape, ':\n', LU[1])
P = permutationMatrix(LU[1])
print('Ma trận hoán vị P', P.shape, ':\n', P)

x = linalg.lu_solve(LU, B)
print("Hệ nghiệm [xi] =", x)
