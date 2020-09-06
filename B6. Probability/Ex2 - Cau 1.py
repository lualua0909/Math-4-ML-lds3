"""============================================================================
   Trong 1 lần kiểm tra, một câu hỏi được đưa ra cho tất cả 30 người tham gia 
   và thời gian được phép trả lời là 25 giây. 
      1. Chọn loại phân phối. Tạo ra (ngẫu nhiên) thời gian trả lời cho 30 người.
      2. Vẽ histogram quan sát. Nhận xét.
      3. Tìm xác xuất 1 người trả lời trong vòng 6 giây. 
         Có bao nhiêu người trong số 30 người trả lời được trong 6 giây.
============================================================================"""
import matplotlib.pyplot as plt
import numpy             as np
import seaborn           as sns

from numpy.random import seed

# 1. Chọn loại phân phối. Tạo ra (ngẫu nhiên) thời gian trả lời cho 30 người.
#    X ~ Uniform(0, 25)
n = 30
a = 0
b = 25

seed(1)
data = np.random.uniform(a, b + 1, n)
data.astype(int)

# 2. Vẽ histogram quan sát. Nhận xét.
plt.figure(figsize = (8, 4))
plt.subplot(1, 2, 1)
plt.hist(data)
plt.subplot(1, 2, 2)
sns.distplot(data, bins = 10, kde = True, color = 'blue',
             hist_kws = {'linewidth': 15,'alpha': 1})
plt.show()

# 3. Tìm xác xuất 1 người trả lời trong vòng 6 giây.
#    F(x) = (x - a) / (b - a)
x    = 6
p_6s = (x - a) / (b - a)
print('P(0 <= x <= 6) =', p_6s)

# Ước lượng số người trả lời trong vòng 6s
print('Số người trả lời trong 6s: ~', round(p_6s * n), 'người')

