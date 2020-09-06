"""============================================================================
   1) Tra XUÔI bảng Z (slide #137)
      a) P(Z < z)
      b) P(z < Z)
      c) P(a < Z < b)

   2) Tra NGƯỢC bảng Z (slide #139)
      d) Xs suy ra giá trị z-score
============================================================================"""

'''----------------------------------------------------------------------------
   Hàm tính xác suất theo phân phối Z (tra XUÔI bảng Z)
----------------------------------------------------------------------------'''
def zDistribution(side, lower, upper):
    import scipy.stats as st

    side = side.lower()
    
    if (side == 'left'):
        p = st.norm.cdf(lower)
    elif (side == 'right'):
        p = 1 - st.norm.cdf(upper)
    else:
        p = st.norm.cdf(upper) - st.norm.cdf(lower)       
    return (p)

'''----------------------------------------------------------------------------
   Hàm tìm z-score khi biết xác xuất (tra NGƯỢC bảng Z)
----------------------------------------------------------------------------'''
def p2z(side, p):
    import scipy.stats as st

    side = side.lower()
    
    if (side == 'left'):
        z = st.norm.ppf(p)
    elif (side == 'right'):
        z = p2z('left', 1 - p)
    else:
        z = p2z('left', 0.5 + (p / 2))
    return (z)

'''----------------------------------------------------------------------------
   Hàm hiển thị xác suất
----------------------------------------------------------------------------'''
def displayZ(side, lower, upper, p):
    side = side.lower()
    lower = str(lower)
    upper = str(upper)
    if (side == 'left'):
        s = 'P(Z < ' + lower + ') = '
    elif (side == 'right'):
        s = 'P(' + upper + ' < Z) = '
    else:
        s = 'P(' + lower + ' < Z < ' + upper + ') = '
    return (s + str('%.4f' %p))



print('---------------------------------')
print('1) Tra XUÔI bảng Z')
print('---------------------------------')
import numpy as np

side  = np.array(['left', 'left', '2-side', '2-side', 'right', 'right'])
lower = np.array([1.2, -0.71, 0, -1.57, None, None])
upper = np.array([None, None, 0.83, 0, 0.44, -0.23])

for i in range(len(side)):
    p = zDistribution(side[i], lower[i], upper[i])
    print(displayZ(side[i], lower[i], upper[i], p))
   
print('---------------------------------')
print('2) Tra NGƯỢC bảng Z')
print('---------------------------------')
side = np.array(['left', 'left', '2-side', '2-side', 'right'])
p    = np.array([0.2119, 0.9948, 0.9030, 0.2052, 0.6915])
for i in range(len(side)):
    z = p2z(side[i], p[i])
    print('p = %.4f' %p[i], '--> z-score = %.2f' %z)
