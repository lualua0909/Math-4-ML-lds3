"""============================================================================
   Tại một trung tâm khai thác dữ liệu, xs thất bại là 0,001 mỗi ngày.  
      1. Chọn loại phân phối. Tạo ra các mẫu (ngẫu nhiên) theo xs trên 
         với số lần lặp lại các thí nghiệm là 365
      2. Vẽ histogram quan sát. Nhận xét.
      3. Hãy cho biết khả năng thất bại trong năm tới là bao nhiêu ?
============================================================================"""
import math
import seaborn as sns

from scipy.stats import bernoulli

# 1. Chọn loại phân phối. Tạo ra các mẫu với 365 lần lặp lại thí nghiệm
#     X ~ Bernoulli(p)
#     p: xác suất thành công
#     size: số lần lặp lại (trials) thí nghiệm.
p          = 0.001
q          = (1 - p)
size       = 1000
data_bernoulli = bernoulli.rvs(size = size, p = p)

# 2. Vẽ histogram quan sát. Nhận xét.
ax = sns.distplot(data_bernoulli, kde = False, color = 'blue',
                  hist_kws = {'linewidth': 15, 'alpha': 1})
ax.set(xlabel = 'Bernoulli Distribution', ylabel = 'Frequency')

# 3. Hãy cho biết khả năng thất bại trong năm tới là bao nhiêu ?
#    P(X = 1) = p
#    P(X = 0) = (1 - p)
#    Thí nghiệm mỗi ngày là độc lập --> tích số 365 lần 
print('P(X = 0, 365 ngày) =', math.pow(q, 365))
