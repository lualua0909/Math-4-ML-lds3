"""=============================================================================
Bài toán: Một thanh tra giao thông đã đếm số lượng ô tô đi qua một điểm nhất định 
          trong 100 khoảng thời gian (cách nhau 20 phút). Các quan sát được liệt kê
          trong tập tin count_cars.txt.
   1. Tạo cars_array từ nội dung tập tin.
   2. Vẽ biểu đồ phân phối tần suất của cars_array
   3. Thống kê cơ bản cho cars_array; 
      mean, median, mode (những giá trị nào? số lần bao nhiêu?), max, min, ...
   4. Tìm range
   5. Cho biết giá trị ở phân vị thứ [5, 15, 25, 50, 75, 90] của cars_array. 
      Biểu diễn phân vị và giá trị tương ứng trên biểu đồ.
   6. Vẽ boxplot của cars_array. 
      Dùng z-score để xác định outliers (indexes nào ? giá trị outliers ?)
   7. Tìm IQR cho car_arrays
   8. Tìm phương sai (variance) cùa cars_array
   9. Tìm độ lệch chuẩn Standard deviation của cars_array
   10. Tìm độ xiên (Skewness) của cars_array. Nhận xét kết quả.
   11. Tìm độ nhọn Kurtosis của cars_array. Nhận xét kết quả.   
============================================================================="""

import numpy             as np
import matplotlib.pyplot as plt
import seaborn           as sns

from numpy import mean, median
from scipy import stats

print('====================================================')
print('*** 1. Tạo mảng dữ liệu chứa từ nội dung tập tin ***')
print('====================================================')
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 5/'
f          = open(folder + 'count_cars.txt', 'r')

content    = f.read()
print('Data:\n', content, '\n')

cars       = content.split()
cars       = list(map(int, cars))
cars_array = np.array(cars)
print('Cars array:\n', cars_array, '\n')

type(cars_array)

print('=======================================================')
print('*** 2. Vẽ biểu đồ phân phối tần suất của dữ liệu    ***')
print('=======================================================')
plt.figure(figsize = (8, 4))
plt.subplot(1, 2, 1)
plt.hist(cars_array)
plt.subplot(1, 2, 2)
sns.distplot(cars_array)
plt.show()

print('================================================')
print('*** 3. Những thống kê cơ bản trên dữ liệu    ***')
print('================================================')
print('Mean   x_    =', mean(cars_array))
print('MIN    x_min =', min(cars_array))
print('MAX    x_max =', max(cars_array))
print('Median x_med =', median(cars_array))
x_mod = stats.mode(cars_array)
print('Mode   x_mod =', x_mod[0][0])
print('       f(x)  =', x_mod[1][0]) # số lần

print('================================================')
print('*** 4. Tìm range                             ***')
print('================================================')
range_cars = np.ptp(cars_array)
print('Range        =', range_cars)

print('================================================')
print('*** 5. Tìm các giá trị bách phân vị          ***')
print('================================================')
percentiles = np.array([5, 15, 25, 50, 75, 90])      # trục tung
x           = np.percentile(cars_array, percentiles) # trục hoành
print('Percentiles =', x)
plt.plot(x, percentiles/100, marker = 'D', color = 'red', linestyle = 'none')
plt.show()

print('========================================================')
print('*** 6. Vẽ boxplot. Dùng z-score để xác định outliers ***')
print('========================================================')
sns.boxplot(cars_array)

z_scores = stats.zscore(cars_array)
print('Z-scores:\n', z_scores)

## outliers
outliers = z_scores[[(n <= -2.5)|(n >= 2.5) for n in z_scores]]
indexes  = [z_scores.tolist().index(i) for i in outliers]
print('Outlier(s) [', indexes, ']:', cars_array[indexes])

print('================================================')
print('*** 7. Tìm IQR                               ***')
print('================================================')
IQR = stats.iqr(cars_array)
print('IQR      =', IQR)

print('================================================')
print('*** 8. Tìm phương sai                        ***')
print('================================================')
var_cars = np.var(cars_array)
print('Variance =', var_cars)

print('================================================')
print('*** 9. Tìm độ lệch chuẩn                     ***')
print('================================================')
std_cars = np.std(cars_array)
print('Std-dev. =', std_cars)

print('================================================')
print('*** 10. Tìm độ nghiêng (skewness)            ***')
print('================================================')
skew_cars = stats.skew(cars_array)
print('Skewness =', skew_cars)

print('================================================')
print('*** 11. Tìm độ nhọn kurtosis. Nhận xét.      ***')
print('================================================')
kur_cars = stats.kurtosis(cars_array) # fisher = True (default) --> (kur - 3)
print('Excess Kurtosis =', kur_cars)

kur_cars = stats.kurtosis(cars_array, fisher = False)
print('Kurtosis        =', kur_cars)

print('Số liệu thống kê:', stats.describe(cars_array))
