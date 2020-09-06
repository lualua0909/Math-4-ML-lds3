"""============================================================================
   Các tham số: 
      - Kích thước quần thể: sP
      - Kích thước mẫu:      sS
      - Số lần lấy mẫu:      n
============================================================================"""
import numpy  as np
import random

from operator import itemgetter

'''----------------------------------------------------------------------------
   Hàm tính các trung bình mẫu
----------------------------------------------------------------------------'''
def sampleMeans(data, n, sS, Mu):
    import numpy as np
    
    result = np.zeros((len(n), 3))
    for t in range(len(n)):
        sampleMeans = []
        for i in range(n[t]):
            # Lấy mẫu S(i) gồm sS cá thể từ quần thể
            sample = random.choices(data, k = sS)
            sampleMeans.append(np.mean(sample))
    
        x_bar = np.mean(sampleMeans)
        result[t, 0] = n[t]
        result[t, 1] = x_bar
        result[t, 2] = abs(Mu - x_bar)
    return result



#==============================================================================
# Kích thước quần thể sP và kích thước mẫu sS    
sP = np.power(10, 6)
sS = 20
n  = [1, 100, 1000, 10000]    # Thay đổi số lần lấy mẫu

print('----------------------------------------------------------------------')
print('1) UNIFORM')
print('----------------------------------------------------------------------')
# Tạo quần thể có chiều cao (cm) nằm trong khoảng [hMin, hMax]
hMin = 145
hMax = 195
data = np.random.uniform(hMin, hMax, sP)
data = data.astype(int) # chuyển sang kiểu INT
Mu   = (hMin + hMax) / 2
print('Kỳ vọng Mu = %.4f' %Mu)

# Phân tích kết quả theo số lần lấy mẫu n
means = sampleMeans(data, n, sS, Mu).tolist()
means = sorted(means, key = itemgetter(2))

for i in range(len(n)):
    print('Lấy mẫu %5d' %means[i][0], 'lần --> trung bình mẫu = %.4f' %means[i][1], 
             '(epsilon = %.4f)' %abs(means[i][2]))

print('\n----------------------------------------------------------------------')
print('2) BINOMIAL')
print('----------------------------------------------------------------------')
# Tạo quần thể từ thí nghiệm n phép thử Bernoulli
trials = 10
p      = 0.3
data   = np.random.binomial(n = trials, p = p, size = sP)
Mu     = (10 * 0.3)
print('Kỳ vọng Mu = %.4f' %Mu)

# Phân tích kết quả theo số lần lấy mẫu n 
means = sampleMeans(data, n, sS, Mu).tolist()
means = sorted(means, key = itemgetter(2))

for i in range(len(n)):
    print('Lấy mẫu %5d' %means[i][0], 'lần --> trung bình mẫu = %.4f' %means[i][1], 
             '(epsilon = %.4f)' %abs(means[i][2]))

print('\n----------------------------------------------------------------------')
print('3) POISSON')
print('----------------------------------------------------------------------')
# Tạo quần thể
lambda_ = 30
data    = np.random.poisson(lam = lambda_, size = sP)
Mu      = lambda_
print('Kỳ vọng Mu = %.4f' %Mu)

# Phân tích kết quả theo số lần lấy mẫu n 
means = sampleMeans(data, n, sS, Mu).tolist()
means = sorted(means, key = itemgetter(2))

for i in range(len(n)):
    print('Lấy mẫu %5d' %means[i][0], 'lần --> trung bình mẫu = %.4f' %means[i][1], 
             '(epsilon = %.4f)' %abs(means[i][2]))

print('\n----------------------------------------------------------------------')
print('4) GEOMETRIC')
print('----------------------------------------------------------------------')
# Tạo quần thể
p    = 0.3
data = np.random.geometric(p = p, size = sP)
Mu   = 1 / p
print('Kỳ vọng Mu = %.4f' %Mu)

# Phân tích kết quả theo số lần lấy mẫu n 
means = sampleMeans(data, n, sS, Mu).tolist()
means = sorted(means, key = itemgetter(2))

for i in range(len(n)):
    print('Lấy mẫu %5d' %means[i][0], 'lần --> trung bình mẫu = %.4f' %means[i][1], 
             '(epsilon = %.4f)' %abs(means[i][2]))
    
print('\n----------------------------------------------------------------------')
print('5) EXPONENTIAL')
print('----------------------------------------------------------------------')
# Tạo quần thể
lambda_ = 30
data    = np.random.exponential(1. / lambda_, size = sP)
Mu      = 1. / lambda_
print('Kỳ vọng Mu = %.4f' %Mu)

# Phân tích kết quả theo số lần lấy mẫu n 
means = sampleMeans(data, n, sS, Mu).tolist()
means = sorted(means, key = itemgetter(2))

for i in range(len(n)):
    print('Lấy mẫu %5d' %means[i][0], 'lần --> trung bình mẫu = %.4f' %means[i][1], 
             '(epsilon = %.4f)' %abs(means[i][2]))

print('\n----------------------------------------------------------------------')
print('6) PARETO')
print('----------------------------------------------------------------------')
# Tạo quần thể
alpha = 3.0   # shape (độ dốc ở phần đầu, gần giá trị của k)
k     = 1     # location hay là giá trị min, default = 0 --> dời curve k đơn vị
data  = np.random.pareto(alpha, sP) + k
Mu    = (k * alpha) / (alpha - 1)
print('Kỳ vọng Mu = %.4f' %Mu)

# Phân tích kết quả theo số lần lấy mẫu n 
means = sampleMeans(data, n, sS, Mu).tolist()
means = sorted(means, key = itemgetter(2))

for i in range(len(n)):
    print('Lấy mẫu %5d' %means[i][0], 'lần --> trung bình mẫu = %.4f' %means[i][1], 
             '(epsilon = %.4f)' %abs(means[i][2]))
