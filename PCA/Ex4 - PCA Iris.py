"""============================================================================
   Ex4: PCA - sklearn
      a) Đọc dữ liệu từ Iris.xls vào dataframe
      b) Tìm correlation matrix, trực quan hóa   
      c) Dùng PCA giảm xuống còn 2 chiều (ban đầu 4 chiều, không kể cột loại iris)
      d) Trực quan hóa dữ liệu sau khi giảm chiều
============================================================================"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# a) Đọc dữ liệu từ Iris.xls vào dataframe
print('\n*** a) Đọc dữ liệu từ Iris.xls vào dataframe:')
# Default folder: 'C:\Users\AnTe'
# Muốn biết [default folder] thì thực hiện [File > Open]
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 3/'
data = pd.read_excel(folder + 'Iris.xls')
print(data.head(), '\n')

# b) Tìm correlation matrix, trực quan hóa
print('\n*** b) Tìm correlation matrix, trực quan hóa:')
corr = data.corr()
print('   - Ma trận hiệp phương sai', corr.shape, ': \n', corr, '\n')
sns.heatmap(corr, xticklabels = corr.columns.values, 
                  yticklabels = corr.columns.values)

# c) Thực hiện giảm chiều dữ liệu xuống còn k = 2, với sklearn.PCA
print('\n*** c) Thực hiện giảm chiều dữ liệu với sklearn.PCA:')
A = data[['sepallength','sepalwidth','petallength','petalwidth']].values
print('   - Ma trận A: \n', A[0:5], '\n')

pca = PCA(2)
pca.fit(A)

# access values and vectors
# components_ : array, shape (n_components, n_features)
# Các trục chính trong không gian feature, biểu thị
# các hướng của phương sai tối đa trong dữ liệu
# explained_variance_ : array, shape (n_components,)
# Số lượng phương sai được giải thích bởi từng thành phần được chọn.
print('PCA.Components:\n', pca.components_)
print('PCA.Shape: ', pca.components_.shape)
print('PCA.Explained variance: ', pca.explained_variance_)
print('PCA.Explained variance shape: ', pca.explained_variance_.shape)

# transform data
B = pca.transform(A)
print('         - Ma trận B_T', B.shape, ': \n', B[0:5], '\n')
print(pca.explained_variance_ratio_)

# d) Trực quan hóa dữ liệu
print('\n*** d) Trực quan hóa dữ liệu:')
plt.scatter(B[:,0], B[:,1])
plt.show()

principalDf = pd.DataFrame(data = B, columns = ['PC 1', 'PC 2'])
print(principalDf.head(), '\n')

y = np.array(data.iris)
y = pd.DataFrame(data = y, columns = ['Types'])
finalDf = pd.concat([principalDf, y], axis = 1)
print('         - Ma trận P', finalDf.shape, ': \n', finalDf[0:5], '\n')

plt.figure(figsize = (8, 8))
sns.scatterplot(x = 'PC 1', y = 'PC 2', data = finalDf)
plt.show()