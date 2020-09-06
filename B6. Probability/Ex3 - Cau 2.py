"""============================================================================
   File [people.txt] chứa nhiệt độ, giới tính, nhịp tim 130 người từ Journal of
   Statistics Education (Shoemaker 1996).
      1. Đọc dữ liệu từ tập tin nói trên.
      2. Vẽ histogram cho cột Tempt.
      3. Tìm thống kê chung của Tempt.
      4. Tìm mean, median, mode => cho nhận xét
      5. Cho biết giá trị Tempt ở phân vị thứ [0, 1, 2, 2.5, 97.5, 98, 99, 100]
      6. Tạo bộ mẫu có 10.000 'temperatures' theo normal distribution 
         với mean, std của bộ dữ liệu trên. Vẽ histogram để quan sát.
      7. Cho biết Three-Sigma-Rules ở các khoảng thứ 1, 2, 3.
      8. Tìm z-score cho thân nhiệt 99.5. Xác định phân vị tương ứng.
============================================================================"""
import matplotlib.pyplot as plt
import numpy             as np
import pandas            as pd
import seaborn           as sns

from scipy.stats import stats, norm

# 1. Đọc dữ liệu vào biến data.
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 6/'
data   = pd.read_csv(folder + '/normtemp.txt', header = None, sep = ' ')

print('Data info    :\n', data.info())
print('Data describe:\n', data.describe())
print('Data         :\n', data.head(), '\n')

# Lấy dữ liệu của các cột 0, 4 và 8
data_n = data[[0, 4, 8]]
print('Data info    :\n', data_n.info())
print('Data describe:\n', data_n.describe())
print('Data         :\n', data_n.head(), '\n')

# Gán tiêu đề cột
data_n.columns = ['Tempt', 'Gender', "Beats"]
print('Data         :\n', data_n.head(), '\n')

# 2. Vẽ histogram cho cột Tempt.
plt.figure(figsize = (6, 6))
sns.distplot(data_n.Tempt)
plt.show()

# 3. Tìm thống kê chung của Tempt.
print('\nSố liệu thống kê:\n', stats.describe(data_n.Tempt))

# $. Tìm mean, median, mode => cho nhận xét
mean_T   = data_n.Tempt.mean()
print('Mean:  ', mean_T)
median_T = data_n.Tempt.median()
print('Median:', median_T)
mode_T   = data_n.Tempt.mode()
print('Mode:  ', mode_T)

# Nhận xét: ~ phân phối khá chuẩn

# 5. Giá trị Tempt ở phân vị thứ [0, 1, 2, 2.5, 97.5, 98, 99, 100]
percentiles = np.array([0, 1, 2, 2.5, 97.5, 98, 99, 100])
x = np.percentile(data_n.Tempt, percentiles)
print('Percentiles[]:', x)

# 6. Tạo bộ mẫu có 10.000 'temperatures' theo normal distribution 
#    với mean, std của bộ dữ liệu trên. Vẽ histogram để quan sát.
#       - loc: mean
#       - scale: standard deviation
#       - size: number of random variates
samples = norm.rvs(size = 10000, loc = mean_T, scale = data_n.Tempt.std())
print(samples)

plt.figure(figsize = (6, 6))
plt.subplot(1, 2, 1)
plt.hist(samples)
plt.subplot(1, 2, 2)
sns.distplot(samples)
plt.show()

# 7. Cho biết Three-Sigma-Rules ở các khoảng thứ 1, 2, 3.
variance = np.var(samples)
print('Var:   ', variance)
std      = variance ** 0.5
print('Std:   ', std)
three_sigma = [std, (std * 2), (std * 3)]
print('3-Sigma:', three_sigma)

std = np.std(samples)
three_sigma = [std, (std * 2), (std * 3)]
print('3-Sigma:', three_sigma)

# 8. Tìm z-score cho thân nhiệt 99.5. Xác định phân vị tương ứng.
#       z-score = (x - mu) / std
x   = 99.5
print('z-score(99.5):', (x - np.mean(samples)) / std)


    

