"""=============================================================================
   Ex3: SVD
   Câu 1: 
      a) Cho tập tin ex3.csv. Đọc tập tin vào dataframe
      b) Phân tích SVD: U, s, VT từ dataframe
      c) Tạo dataframe mới từ U, s, VT, nhận xét và rút gọn thành phần, nếu có thể
      d) Tìm error nếu có rút gọn thành phần 
============================================================================="""
import numpy  as np
import pandas as pd

LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 2/'

## a) Đọc tập tin ex3.csv vào dataframe
df = pd.read_csv(folder + 'ex3.csv', index_col = 0)
print('\n*** a) Dataframe ex3.csv:\n', df, '\n')

## b) Phân tích SVD: U, s, VT
U, s, VT = np.linalg.svd(df)

print('\n*** b) Phân tích SVD:')
print('- Ma trận U(', U.shape[1], ', ', U.shape[0], '): \n', U, '\n')
print('- Eigenvalues:', s, '\n')
print('- Ma trận VT(', VT.shape[1], ', ', VT.shape[0], '): \n', VT, '\n')

## c) Tạo dataframe mới từ U, s, VT
col_headers = ['post1', 'post2', 'post3', 'post4']
words = ['ice', 'snow', 'tahoe', 'goal', 'puck']
new_df = pd.DataFrame(VT, columns = col_headers)
A_approx = np.matrix(U[:, :2]) * np.diag(s[:2]) * np.matrix(VT[:2, :])

print('\n*** c) NEW dataframe (using only the first two components):')
print(pd.DataFrame(A_approx, index = words, columns = col_headers))

## d) Tìm error
print("\n*** d) Error from actual value:")
print(df - A_approx)

## e) Hiển thị
import matplotlib.pyplot as plt

plt.imshow(VT, interpolation = 'none')
plt.xticks(range(len(col_headers)))
plt.yticks(range(len(words)))
plt.ylim([len(words) - 1.5, -.5])
ax = plt.gca()
ax.set_xticklabels(col_headers)
ax.set_yticklabels(range(1, len(words) + 1))
plt.title("$V$")
plt.colorbar()


