"""============================================================================
   Ex2: PCA - sklearn
      a) Đọc dữ liệu từ student.xlsx vào dataframe
      b) Thực hiện giảm chiều dữ liệu với sklearn.PCA
      c) Trực quan hóa dữ liệu
============================================================================"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# a) Đọc dữ liệu từ student.xlsx vào dataframe
print('\n*** a) Đọc dữ liệu từ student.xlsx vào dataframe:')

# Default folder: 'C:\Users\AnTe'
# Muốn biết [default folder] thì thực hiện [File > Open]
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 3/'

data       = pd.read_excel(folder + 'student.xlsx', index_col = 0)
print(data.head(), '\n')

# b) Thực hiện giảm chiều dữ liệu xuống còn k = 2, với sklearn.PCA
print('\n*** b) Thực hiện giảm chiều dữ liệu với sklearn.PCA:')
pca = PCA(2)
pca.fit(data)

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
B = pca.transform(data)
print('         - Ma trận B_T', B.shape, ': \n', B[0:5], '\n')
print(pca.explained_variance_ratio_)

principalDf = pd.DataFrame(data = B, columns = ['PC 1', 'PC 2'])
print(principalDf.head(), '\n')

# c) Trực quan hóa dữ liệu
print('\n*** c) Trực quan hóa dữ liệu:')
plt.figure(figsize = (8, 6))
sns.jointplot(x = 'PC 1', y = 'PC 2', data = principalDf)              
plt.show()
