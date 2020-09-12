"""============================================================================
   Slides #35 --> #37
      n   : số lần thí nghiệm
      p   : xác suất thành công
      size: số mẫu thử
============================================================================"""
import math
import seaborn as sns

from scipy.stats import binom
from scipy.stats import stats

# n đủ lớn, p = 0.5 ==> xấp xỉ phân phối chuẩn
n    = 12
p    = 0.5
size = 1000
probs = [0.3, 0.5, 0.8] 
# data_binom = [binom.rvs(n = n, p = p, size = size) for p in probs]
data_binom = binom.rvs(n = n, p = p, size = size)

ax = sns.distplot(data_binom, kde = False, color = 'blue',
                  hist_kws = {'linewidth': 15, 'alpha':1})
ax.set(xlabel = 'Binomial Distribution', ylabel = 'Frequency')

print('\nSố liệu thống kê:\n', stats.describe(data_binom))

# Thí nghiệm tung đồng xu: mặt sấp hoặc mặt ngửa
#    - Giả sử tung một đồng xu 'công bằng' 12 lần. Tính xác suất để có 7 lần ngửa.
#
#    P_x_k = n!/(k!)(n - k)! x p^k x (1 - p)^(n - k)

k = 7
C_n_k = math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
P_X_k =  C_n_k * math.pow(p, k) * math.pow(1 - p, n - k)

print('P(X = 7) = %.4f' %P_X_k)

# Dùng hàm của python
print('P(X = 7) = %.4f (PYTHON)' %binom.pmf(k, n, p, loc = 0))
