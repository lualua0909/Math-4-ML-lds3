"""============================================================================
   Ex2: PCA - sklearn --> mở rộng thêm phân tích phương sai để xác định k
      a) Đọc tập tin dữ liệu Student_12f.xls vào dataframe.
      b) Áp dụng phương pháp PCA để giảm xuống k chiều (2 < k < 12).
         Giải thích nguyên nhân hay cơ sở về số chiều được giảm.
      c) Giảm chiều xuống còn k = 2 và trực quan hóa dữ liệu. Nhận xét kết quả.
============================================================================"""
import matplotlib.pyplot as plt
import numpy             as np
import pandas            as pd
import seaborn           as sns

from sklearn.decomposition import PCA

print('============================================================')
print('*** a) Đọc tập tin dữ liệu Student_12f.xls vào dataframe ***')
print('============================================================')

# Default folder: 'C:\Users\AnTe'
# Muốn biết [default folder] thì thực hiện [File > Open]
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 3/'
data       = pd.read_excel(folder + 'Student_12f.xls')
print(data.head(), '\n')

print('=============================================================')
print('*** b) Áp dụng PCA để giảm xuống còn k chiều (2 < k < 12) ***')
print('=============================================================')
#   https://stackoverflow.com/questions/32857029/python-scikit-learn-pca-explained-variance-ratio-cutoff
#   - The pca.explained_variance_ratio_ returns a vector of the variance explained by each dimension.
#   - The pca.explained_variance_ratio_[i] gives the variance explained solely by the i+1st dimension.
#   - The pca.explained_variance_ratio_.cumsum() will return a vector x 
#     such that x[i] returns the cumulative variance explained by the first i+1 dimensions.

#   (1) PCA().components_: Chuyển vị của ma trận vectơ riêng EigenVectors.T
#   (2) PCA().explained_variance_: Các giá trị riêng
#   (3) PCA().explained_variance_ratio_: Tỷ lệ phương sai so với dữ liệu gốc
#   (4) Hàm numpy.cumsum()

#-------------------------------------------------------------
# CÁCH 1: Chọn k dựa trên đồ thị biểu diễn phương sai tích lũy
#-------------------------------------------------------------
print('CÁCH 1: Chọn k dựa trên đồ thị biểu diễn phương sai tích lũy')
pca = PCA().fit(data)

# Vẽ đồ thị biểu diễn % phương sai tích lũy theo số features
plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Số lượng features')
plt.ylabel('Variance (%)')
plt.title('Đồ thị biểu diễn % phương sai tích lũy theo số features')
plt.show()

# Nhận xét:
#   - #f =  0: giữ lại    0%  phương sai so với dữ liệu gốc
#   - #f =  3: giữ lại ~ 85%  phương sai so với dữ liệu gốc
#   - #f >  3: giữ lại > 90%  phương sai so với dữ liệu gốc
#   - #f = 12: giữ lại   100% phương sai so với dữ liệu gốc
#

print('Phân tích chi tiết theo k:')
for k in range(1, 13):
    pca = PCA(k)
    pca.fit(data)
      
    var = pca.explained_variance_ratio_.sum() * 100
    print('   * k = %2d' %k, '--> phương sai tích lũy %.0f%%' %var)

    # Test - BEGIN
    print('- Chuyển vị của ma trận vectơ riêng P_T', pca.components_.shape, ': \n', 
                                                     pca.components_, '\n')
    print('- Ma trận trị riêng LAMBDA', pca.explained_variance_.shape, ': \n', 
                                        pca.explained_variance_, '\n')   
    # Test - END


#---------------------------------------------------------------
# CÁCH 2: Chọn k dựa trên ngưỡng phương sai (tích lũy) mong muốn
#---------------------------------------------------------------
print('\nCÁCH 2: Chọn k dựa trên ngưỡng phương sai (tích lũy) mong muốn')
# Giả sử muốn giữ lại 90%
threshold = .9
percent   = threshold * 100
pca       = PCA(threshold)

pca.fit(data)
k   = pca.n_components_
var = sum(pca.explained_variance_ratio_) * 100
print('   Muốn phương sai tích lũy >= %.0f%%' %percent, 'thì k >= %d' %k,
      ' (k = %d' %k, '--> %.0f%%)' %var)

print('\nPhân tích chi tiết theo ngưỡng phương sai:')
A = np.array([.5, .6, .7, .8, .9, .95, .99])
for x in A:
    percent   = x * 100
    pca       = PCA(x)

    pca.fit(data)
    k   = pca.n_components_
    var = sum(pca.explained_variance_ratio_) * 100
    print('   Muốn phương sai tích lũy >= %.0f%%' %percent, 'thì k >= %2d' %k,
          ' (k = %2d' %k, '--> %.0f%%)' %var)

print('========================================================')
print('*** c) Giảm chiều còn k = 2 và trực quan hóa dữ liệu ***')
print('========================================================')
k   = 2
pca = PCA(k)
pca.fit(data)

# transform data
B = pca.transform(data)
print('- Ma trận B_T', B.shape)

principalDf = pd.DataFrame(data = B, columns = ['Component 1', 'Component 2'])
print(principalDf.head(), '\n')

plt.figure(figsize = (8, 6))
sns.jointplot(x = 'Component 1', y = 'Component 2', data = principalDf)              
plt.show()
