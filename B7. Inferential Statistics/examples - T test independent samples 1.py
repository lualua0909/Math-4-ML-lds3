"""============================================================================
   Slides #76
      - H0: The means are equal
============================================================================"""

from scipy import stats

data1 = [ 1, 2, 2, 3, 3, 4, 4, 5, 5, 6 ]
data2 = [ 1, 2, 4, 5, 5, 5, 6, 6, 7, 9 ]

t, p = stats.ttest_ind(data1, data2)

print('T-test:\n', stats.ttest_ind(data1, data2))

alpha = 0.05   
if (p > alpha):
    print('(p >  alpha) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(p <= alpha) ==> REJECT the H0 that the means are equal.')
    
