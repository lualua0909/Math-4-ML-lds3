"""============================================================================
   Ex1: Tính toán PCA
      a) Tạo một ma trận A(3000, 3) có các giá trị ngẫu nhiên từ 1 đến 255
      b) Áp dụng tính toán PCA
      c) Trực quan hóa kết quả 
============================================================================"""
import numpy as np
from numpy import mean
from numpy import cov
from numpy.linalg import eig
# import matplotlib.pyplot as plt

# a) Tạo ma trận có các giá trị "ngẫu nhiên"
print('\n*** a) Tạo ma trận có các giá trị ngẫu nhiên từ 1 đến 255:')
# set random seed to repeat
np.random.seed(190)
A = np.random.randint(1, 256, (3000,3))
print('         - Matrix A', A.shape, ': \n', A[0:10], '\n')

print('\n*** b) Tính PCA:')
# column means\n",
M = mean(A.T, axis = 1)
print('         - Mean vectors M:', M, '\n')

# center columns by subtracting column means
C = A - M
print('         - Center matrix C', C.shape, ': \n', C[0:10], '\n')

# calculate covariance matrix of centered matrix
V = cov(C.T)
print('         - Covariance matrix V', V.shape, ': \n', V, '\n')

# factorize covariance matrix
eigenvalues, eigenvectors = eig(V)

print('\n*** b) Eigendecomposition:')
print('         - Eigenvectors P', eigenvectors.shape, ': \n', eigenvectors, '\n')
print('         - Eigenvalues Lambda', eigenvalues.shape, ': \n', eigenvalues, '\n')

# project data
P = eigenvectors.T.dot(C.T)
print(P.T)

