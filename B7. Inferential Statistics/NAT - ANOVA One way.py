"""=============================================================================
   Phương pháp One way ANOVA: 
       - Tính toán theo các công thức SSW và SSB
       - Dùng các hàm của scipy.stats
============================================================================="""
import numpy       as np
import pandas      as pd
import scipy.stats as stats

alpha = 0.05

##------------------------------------------------------------------------------
## Chuẩn bị dữ liệu
##------------------------------------------------------------------------------
## Kích thước của các mẫu có thể KHÁC NHAU
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Datasets/One way ANOVA/'

fname      = 'Excavation Depth and Archaeology.txt'
d          = pd.read_csv(folder + fname, sep = '\t')

## Xác định k nhóm là k cột trong tập dữ liệu
# groupsA = list(d.columns.values) # array
k      = len(d.columns)
groups = list(d.columns) # (k column headers)

## Tạo k mẫu (loại bỏ giá trị NaN trong các mẫu)
samples = []
for j in range(k):
    sample = [x for x in d[groups[j]] if pd.notnull(x)]
    samples.append(sample)

##------------------------------------------------------------------------------
print('----------- Cách 1: Tính toán "truyền thống" theo các công thức ---------')
##------------------------------------------------------------------------------    
## Số phần tử của mỗi nhóm
sizes = np.zeros(k)
for j in range(k): 
    sizes[j] = np.size(samples[j])

## Giá trị trung bình của mỗi mẫu
means = np.zeros(k)
for j in range(k):
    means[j] = np.mean(samples[j])

## Giá trị trung bình của tất cả các mẫu
meanT = np.mean(means)

## Các đại lượng BETWEEN groups: SSB, dfB
SSB = 0
for j in range(k):
    SSB += sizes[j] * np.power((means[j] - meanT), 2)
dfB = (k - 1)
print('SSB           : %.4f' %SSB)
print('dfB           : %d' %dfB)
   
## Các đại lượng WITHIN groups: SSW, dfW
SSW = 0
for j in range(k):
    SSWj = 0
    for i in range(int(sizes[j])):
        SSWj += np.power(samples[j][i] - means[j], 2)
    SSW += SSWj
dfW = int(np.sum(sizes) - k)
print('SSW           : %.4f' %SSW)
print('dfW           : %d' %dfW)

## Trị thống kê: F statistics
F = (SSB / dfB) / (SSW / dfW)
print('F statistic   : %.4f' %F)

## Giá trị tới hạn
##------------------------------------------------------------------------------
## Hàm scipy.stats.f.ppf(q, dfn, dfd) xác định giá trị tới hạn
##    q  : confidence level     (1 - alpha)
##    dfn: tử số (numerator)    dfB (BETWEEN groups)
##    dfd: mẫu số (denominator) dfW (WITHIN groups)
##
## Hàm scipy.stats.f.cdf(crit, dfn, dfd) xác định confidence level (1 - alpha)
##------------------------------------------------------------------------------
critical_value = stats.f.ppf(q = 1 - alpha, dfn = dfB, dfd = dfW)
print('Critical value: %.4f' %critical_value)
conf_level     = stats.f.cdf(critical_value, dfn = dfB, dfd = dfW)

if (F < critical_value):
    print('(F <  critical value) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(F >= critical value) ==> REJECT the H0 that the means are equal.')

##------------------------------------------------------------------------------
print('\n--------------------- Cách 2: Sử dụng hàm của Python ------------------')
##------------------------------------------------------------------------------    
fvalue, pvalue = stats.f_oneway(samples[0], samples[1], samples[2], samples[3])

print('p-value       : %.4f' %pvalue)
print('F statistic   : %.4f' %fvalue)

