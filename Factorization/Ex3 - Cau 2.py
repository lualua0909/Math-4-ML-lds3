"""=============================================================================
   Ex3: SVD
   Câu 2: 
      a) Cho tập tin iris.csv, đọc dữ liệu ra dataframe và chỉ lấy 4 cột đầu
      b) Phân tích SVD: U, s, VT từ dataframe
      c) Tạo dataframe mới từ U, s, VT, nhận xét và rút gọn thành phần, nếu có thể
      d) Tìm error nếu có rút gọn thành phần 
      e) Tái cấu trúc dataframe theo U, s, VT (giữ nguyên tất cả các thành phần)
============================================================================="""
import numpy as np
import pandas as pd

LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 2/'

## a) Đọc tập tin iris vào dataframe
iris = pd.read_csv(folder + 'iris.csv')
print('\n*** a) Dataframe iris.csv:\n', iris.head())

X = iris[['sepal_length','sepal_width','petal_length','petal_width']]
print('\n       - 4 cột đầu tiên:\n', X.head())

## b) Phân tích SVD: U, s, VT
U, s, VT = np.linalg.svd(X)

print('\n*** b) Phân tích SVD:')
print('         - Ma trận U(', U.shape[1], ', ', U.shape[0], '): \n', U, '\n')
print('         - Eigenvalues:', s, '\n')
print('         - Ma trận VT(', VT.shape[1], ', ', VT.shape[0], '): \n', VT, '\n')

## c) Tạo dataframe mới từ U, s, VT
X1 = np.matrix(U[:, :2]) * np.diag(s[:2]) * np.matrix(VT[:2, :])

print('\n*** c) NEW dataframe (using only the first two components):')
print('         - X1.shape():', X1.shape)
Xnew = pd.DataFrame(X1, index = X.index, columns = X.columns)
print(Xnew.head())

## d) Tìm error
print('\n*** d) Error from actual value:')
print((X - X1).head())

## e) Tái tạo ma trận
Sigma = np.zeros_like(X)
Sigma[:X.shape[1], :X.shape[1]] = np.diag(s)
print(Sigma.shape)

X_c = U.dot(Sigma.dot(VT))
print(X_c[0:5])

X_c_new = pd.DataFrame(X_c, columns = X.columns)
print(X_c_new.head())

