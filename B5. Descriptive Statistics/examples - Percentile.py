"""=============================================================================
   Minh họa: Bách phân vị
============================================================================="""
import math
import numpy as np

##------------------------------------------------------------------------------
## Hàm tính bách phân vị thứ p của dãy số
##    rank = (p * n) / 100
##------------------------------------------------------------------------------
def percentile1(data, p):
    
    data = sorted(data)
    size = len(data)

    if (p == 0):
        value = data[0]
    elif (p == 100):
        value = data[size - 1]
    else:
        # Tính chỉ số rank
        i = (p * size) / 100
        k = int(i)
    
        # Tính phân vị thứ p
        if (k == i):
            print('i =', i, 'k =', k)
        
            value = (data[k - 1] + data[k]) / 2
        else:
            value = data[k]

        ## Interpolation
        ## f = i - k
        ## value = ((1 - f) * x[k - 1]) + (f * x[k])
    return value

def percentile2(data, p):
    size = len(data)
    return sorted(data)[int(math.ceil((size * p) / 100)) - 1]

def percentile_python(x, p):
    x = sorted(x)
    percentiles = np.zeros(5)
    percentiles[0] = np.percentile(x, p)        # Default: linear
    percentiles[1] = np.percentile(x, p, interpolation = 'lower')
    percentiles[2] = np.percentile(x, p, interpolation = 'higher')
    percentiles[3] = np.percentile(x, p, interpolation = 'midpoint')
    percentiles[4] = np.percentile(x, p, interpolation = 'nearest')
   
    return percentiles
##------------------------------------------------------------------------------

## 
x = np.array([8, 9, 12, 14.5, 15.5, 17, 18])
p = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

print('\n** Sử dụng hàm np.percentile()')
##------------------------------------------------------------------------------
## INTERPOLATION parameter --> khi rank = 1 + (p * (n - 1)) / 100 không là số nguyên,
##    rank thuộc khoảng (l, u)
##    ‘linear’: l + (u - l) * f; (f là phần thập phân của rank)
##    ‘lower’: l
##    ‘higher’: u
##    ‘midpoint’: (l + u) / 2
##    ‘nearest’: làm tròn rank
##------------------------------------------------------------------------------
percentiles = np.zeros((len(p), 6))

for i in range(0, len(p)):
    print('  Bách phân vị P%d =' %p[i], percentile_python(x, p[i]))


print('\n** Sử dụng công thức')
for i in range(0, len(p)):
    print('  Bách phân vị P%d =' %p[i], percentile1(x, p[i]))

x = np.array([3650, 3730, 3355, 3450, 3480, 3480, 3490, 3520, 3310, 3540, 3550, 3925])
