"""============================================================================
   Sinh viên nam tại một trường đại học X có chiều cao trung bình là 164cm.
   Các chiều cao thường được phân phối, với độ lệch chuẩn là 6cm.
   Cho biết giá trị ở phân vị thứ [99] của bộ mẫu.
      1. Tạo ra 1000 mẫu (ngẫu nhiên) theo mô tả trên.
      2. Vẽ histogram quan sát. Nhận xét.
      3. Cho biết giá trị ở phân vị thứ [99] của bộ mẫu.
      4. Tìm z-score cho chiều cao 174cm. Xác định phân vị tương ứng.
============================================================================"""
import numpy     as np
import seaborn   as sns

from scipy.stats import norm

# 1. Tạo ra 1000 mẫu (ngẫu nhiên) theo mô tả trên: X ~ N(mu = 164, sigma = 6)
#    - loc: mean
#    - scale: standard deviation
#    - size: number of random variates
mean        = 164
std         = 6
data_normal = norm.rvs(size = 1000, loc = mean, scale = std)
print(data_normal)

# 2. Vẽ histogram quan sát. Nhận xét.
ax = sns.distplot(data_normal, bins = 100, kde = True, color = 'blue',
                  hist_kws = {'linewidth': 15,'alpha':1})
ax.set(xlabel = 'Normal distribution', ylabel = 'Frequency')
    
# 3. Cho biết giá trị ở phân vị thứ [99] của bộ mẫu.
P99 = np.array([99])
x   = np.percentile(data_normal, P99)
print('P99:', x)

# 4. Tìm z-score cho chiều cao 174cm. Xác định phân vị tương ứng.
#       z-score = (x - mu) / std
x   = 174
print('z-score(174):', (x - mean) / std)
