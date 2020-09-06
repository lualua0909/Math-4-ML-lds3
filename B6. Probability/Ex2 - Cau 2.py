"""============================================================================
   Có 60% người mua xe thể thao là nam giới.  
      1. Chọn loại phân phối. Tạo ra 10 mẫu (ngẫu nhiên) theo mô tả trên 
         với số lần lặp lại các thí nghiệm là 1000
      2. Vẽ histogram quan sát. Nhận xét.
      3. Trong 10 chủ xe thể thao được chọn ngẫu nhiên, tính xs có 7 nam giới.
============================================================================"""
import math
import seaborn as sns

from scipy.stats import binom

#------------------------------------------------------------------------------
#  Hàm tính tổ hợp n chập k
#  Vơi Python 3.8 thì dùng math.comb(n, k)
#------------------------------------------------------------------------------
def combination(n, k):
    # n!/(k!)(n-k)!
    numerator   = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n - k)

    return (numerator / denominator)


# 1. Chọn loại phân phối. Tạo ra 10 mẫu với 1000 lần lặp lại thí nghiệm
#     X ~ Binomial(n, p)
#     n: số mẫu thử nghiệm
#     p: xác suất thành công
#     size: số lần lặp lại (trials) thí nghiệm.
n          = 10
p          = 0.6
size       = 1000
data_binom = binom.rvs(n=n, p=p, size = size)

# 2. Vẽ histogram quan sát. Nhận xét.
ax = sns.distplot(data_binom, kde = False, color = 'blue',
                  hist_kws = {'linewidth': 15, 'alpha': 1})
ax.set(xlabel = 'Binomial Distribution', ylabel = 'Frequency')

# 3. Trong 10 chủ xe thể thao được chọn ngẫu nhiên, tính xs có 7 nam giới.
#    f(k) = P(X = k) = P_x = n!/(k!)(n-k)! x p^k x (1-p)^(n-k)
k     = 7
P_X_k = combination(n, k) * math.pow(p, k) * math.pow(1 - p, n - k)
print('P(X = 7) =', P_X_k)


