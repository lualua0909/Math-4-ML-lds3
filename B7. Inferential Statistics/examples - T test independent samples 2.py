"""============================================================================
   Slides #83, #84, #85
      - H0: The means are equal
============================================================================"""
from math         import sqrt
from numpy        import mean
from numpy.random import seed, randn

from scipy.stats import sem, t, ttest_ind

'''----------------------------------------------------------------------------
   Cách 1: Tính toán truyền thống             
----------------------------------------------------------------------------'''

#------------------------------------------------------------------------------
# Function for calculating the t-test for two independent samples
#------------------------------------------------------------------------------
def independent_T_test(data1, data2, alpha):
    # Calculate 2 means
    mean1, mean2 = mean(data1), mean(data2)
    
    # Calculate 2 standard errors (SEM)
    se1, se2 = sem(data1), sem(data2)
    
    # Standard error on the difference between the samples
    sed = sqrt(se1**2.0 + se2**2.0)
    
    # Calculate the t statistic
    t_stat = (mean1 - mean2) / sed
    
    # Degrees of freedom
    df = len(data1) + len(data2) - 2
    
    # Calculate the critical value
    cv = t.ppf(1.0 - alpha, df)
    
    # Calculate the p-value
    p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
    
    # Return everything
    return t_stat, df, cv, p


#------------------------------------------------------------------------------
# Calculate the t test
#------------------------------------------------------------------------------

# Data
seed(1)

# Generate two independent samples
data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 50
    
alpha = 0.05

t_stat, df, cv, p = independent_T_test(data1, data2, alpha)
print('t = %.3f, df = %d, cv = %.3f, p = %.3f' % (t_stat, df, cv, p))

# Interpret via critical value
if abs(t_stat) <= cv:
    print('(t <= critical value) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(t >  critical value) ==> REJECT the H0 that the means are equal.')

# Interpret via p-value
if (p > alpha):
    print('(p >  alpha) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(p <= alpha) ==> REJECT the H0 that the means are equal.')
    

'''----------------------------------------------------------------------------
   Cách 2: Sử dụng scipy.stats import ttest_ind             
----------------------------------------------------------------------------'''

t_stat, p = ttest_ind(data1, data2)
print('\nt = %.3f, p = %.3f' % (t_stat, p))

# Interpret via p-value
if (p > alpha):
    print('(p >  alpha) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(p <= alpha) ==> REJECT the H0 that the means are equal.')
    
