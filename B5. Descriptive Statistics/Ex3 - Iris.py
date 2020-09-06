"""=============================================================================
Cho dữ liệu Iris.xls
   1. Đọc dữ liệu vào biến data.
   2. Xem thông tin data: info, describe, head.
   3. Tính chiều cao trung bình của petallength, loại hoa Iris versicolor.
   4. Tạo array phần trăm percentiles chứa các phần trăm thứ 2.5, 25, 50, 75, 97.5.
      Tính percentiles của petal lengths từ các mẫu Iris versicolor.
   5. Vẽ percentiles với marker='D', color='red', x và y tương ứng là ptiles_vers và percentiles/100.
   6. Tạo array differences: chênh lệch giữa petallength với mean petallength. 
      Tính bình phương differences. 
      Tính mean square difference và đặt tên là variance_explicit.
   7. Tính variance trên bằng cách sử dung np.var. So sánh kết quả.
   8. Tính căn bậc hai của variance ở câu trên.
   9. Tính độ lệch chuẩn của petallength.
   10. Vẽ biểu đồ thể hiện mối quan hệ của versicolor_petal_length, versicolor_petal_width.
   11. Tìm covariance matrix của versicolor_petal_length, versicolor_petal_width. 
       Trích xuất covariance của petallength và petalwidth từ covariance matrix 
       và đặt tên là petal_cov.
   12. Tìm correlation matrix của versicolor_petal_length, versicolor_petal_width.
       Trích xuất correlation của petallength và petalwidth từ correlation matrix 
       và đặt tên là petal_corr.
   13. Vẽ boxplot của pentallength cho toàn bộ data và của pentallength theo loại.
   14. Dựa trên boxplot trên, hãy cho biết các loại có outlier(s) không?
       Nếu có, dùng z-score để tính và xác định index của outlier(s) theo từng loại 
       (những index nào? giá trị outliers tương ứng cho những index đó?)
   15. Cho các biểu đồ sau:
       from PIL import Image
       import matplotlib.pyplot as plt
       import numpy as np
       img = np.array(Image. open('map1.jpg'))
       plt.figure(figsize=(12,12))
       plt. imshow(img, interpolation='bilinear' )
       plt. axis('off' )
       plt. show()
    Xác định biểu đồ nào có:
       - variance cao nhất trên x
       - covariance cao nhất
       - negative covariance
============================================================================="""
import numpy             as np
import matplotlib.pyplot as plt
import pandas            as pd
import seaborn           as sns

from scipy import stats

print('====================================================')
print('*** 1. Tạo mảng dữ liệu chứa từ nội dung tập tin ***')
print('====================================================')
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 5/'
data       = pd.read_excel(folder + '/Iris.xls')

print('====================================================')
print('*** 2. Xem thông tin data: info, describe, head. ***')
print('====================================================')
print('Data info    :\n', data.info())
print('Data describe:\n', data.describe())
print('Data         :\n', data.head(), '\n')

print('================================================================')
print('*** 3. Chiều cao trung bình của petallength Iris versicolor. ***')
print('================================================================')
pental_lenghth_Iris_versicolor = data[data.iris == 'Iris-versicolor']['petallength']

mean_pental_lenghth = pental_lenghth_Iris_versicolor.mean()
print(mean_pental_lenghth)

## 4. Tạo array phần trăm percentiles chứa các phần trăm thứ 2.5, 25, 50, 75, 97.5.
##    Tính percentiles của petal lengths từ các mẫu Iris versicolor.
percentiles = np.array([2.5, 25, 50, 75, 97.5])
ptiles_vers = np.percentile(pental_lenghth_Iris_versicolor, percentiles)

## 5. Vẽ percentiles với marker='D', color='red', x và y tương ứng là ptiles_vers và percentiles/100.
plt.plot(ptiles_vers, percentiles/100, marker = 'D', color = 'red', linestyle = 'none')
plt.show()

## 6. Tạo array differences: chênh lệch giữa petallength với mean petallength. 
##      Tính bình phương differences. 
##      Tính mean square difference và đặt tên là variance_explicit.
differences = pental_lenghth_Iris_versicolor - mean_pental_lenghth
print(differences[0:10])

diff_sq = differences**2
print(diff_sq[0:10])

variance_explicit = np.mean(diff_sq)
print(variance_explicit)

## 7. Tính variance trên bằng cách sử dung np.var. So sánh kết quả.
variance = np.var(pental_lenghth_Iris_versicolor)
print(variance)

## 8. Tính căn bậc hai của variance ở câu trên.
print(np.sqrt(variance))

## 9. Tính độ lệch chuẩn của petallength.
print(np.std(pental_lenghth_Iris_versicolor))

## 10. Vẽ biểu đồ thể hiện mối quan hệ của versicolor_petal_length, versicolor_petal_width.
pental_width_Iris_versicolor = data[data.iris == 'Iris-versicolor']['petalwidth']

plt.figure(figsize =(8, 6))
plt.plot(pental_lenghth_Iris_versicolor, pental_width_Iris_versicolor,
         marker = '.', linestyle = 'none')
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.show()

## 11. Tìm covariance matrix của versicolor_petal_length, versicolor_petal_width. 
##     Trích xuất covariance của petallength và petalwidth từ covariance matrix 
##     và đặt tên là petal_cov.
covariance_matrix = np.cov(pental_lenghth_Iris_versicolor, pental_width_Iris_versicolor)
print(covariance_matrix)
petal_cov = covariance_matrix[0, 1]
print(petal_cov)

## 12. Tìm correlation matrix của versicolor_petal_length, versicolor_petal_width.
##     Trích xuất correlation của petallength và petalwidth từ correlation matrix 
##     và đặt tên là petal_corr.
corr_matrix = np.corrcoef(pental_lenghth_Iris_versicolor, pental_width_Iris_versicolor)
print(corr_matrix)
petal_corr = corr_matrix[0, 1]
print(petal_corr)

## 13. Vẽ boxplot của pentallength cho toàn bộ data và của pentallength theo loại.
plt.figure(figsize = (8, 6))
sns.boxplot(x = 'iris', y = 'petallength', data = data)
plt.xlabel('Species')
plt.ylabel('Petal length (cm)')
plt.show()

plt.figure(figsize = (8, 6))
plt.boxplot(data.petallength)
plt.ylabel('Petal length (cm)')
plt.show()

## 14. Dựa trên boxplot trên, hãy cho biết các loại có outlier(s) không?
##       Nếu có, dùng z-score để tính và xác định index của outlier(s) theo từng loại 
##       (những index nào? giá trị outliers tương ứng cho những index đó?)
''' Nhận xét:
    - Iris-virginica không có outlier
    - Iris-setosa và Iris-versicolor có outliers
'''
pental_lenght_Iris_setosa = data[data.iris == 'Iris-setosa']['petallength']
pental_lenght_Iris_setosa[0:5]

number_z_score_setosa = stats.zscore(pental_lenght_Iris_setosa)
print(number_z_score_setosa)
print(pental_lenght_Iris_setosa.index)

## vì index của nhóm này là từ 0 nên không cần tình lại index
outliers_setosa = number_z_score_setosa[[(n <=-2.5)|(n>=2.5) for n in number_z_score_setosa]]
indexes_setosa = [number_z_score_setosa.tolist().index(i) for i in outliers_setosa]
print("Indexes:", indexes_setosa)
print("Outliers:\n", pental_lenght_Iris_setosa[indexes_setosa])

## Ouliers of Iris-versicolor
number_z_score_versicolor = stats.zscore(pental_lenghth_Iris_versicolor)
print(number_z_score_versicolor)
print(pental_lenghth_Iris_versicolor.index)

## vì index của nhóm này là từ 50 nên +50 để biết index chính xác
outliers_versicolor = number_z_score_versicolor[[(n <=-2.5)|(n>=2.5) for n in number_z_score_versicolor]]
indexes_versicolor = [number_z_score_versicolor.tolist().index(i) for i in outliers_versicolor]
indexes_versicolor = [ value + 50 for value in indexes_versicolor]
print("Indexes:", indexes_versicolor)
print("Outliers:\n", pental_lenghth_Iris_versicolor[indexes_versicolor])

## 15: 
##       - variance cao nhất trên x: d)
##       - covariance cao nhất     : c)
##       - negative covariance     : b)