"""============================================================================
   Slides #86, #87, #88, #89
      - H0: The means are equal
============================================================================"""
from math         import sqrt
from numpy        import mean
from numpy.random import seed, randn

from scipy.stats import t, ttest_rel

'''----------------------------------------------------------------------------
   Cách 1: Tính toán truyền thống             
----------------------------------------------------------------------------'''

#------------------------------------------------------------------------------
# Function for calculating the t-test for two DEPENDENT samples
#------------------------------------------------------------------------------
def dependent_T_test(data1, data2, alpha):
  
    # Calculate 2 means
    mean1, mean2 = mean(data1), mean(data2)
    
    # Number of paired samples
    n = len(data1)
    
    # Sum squared difference between observations
    d1 = sum([(data1[i] - data2[i])**2 for i in range(n)])
    
    # Sum difference between observations
    d2 = sum([data1[i] - data2[i] for i in range(n)])
    
    # Standard deviation of the difference between means
    sd = sqrt((d1 - (d2**2 / n)) / (n - 1))
    
    # Standard error of the difference between the means
    sed = sd / sqrt(n)
    
    # Calculate the t statistic
    t_stat = (mean1 - mean2) / sed

    # Degrees of freedom
    df = n - 1

    # Calculate the critical value
    cv = t.ppf(1.0 - alpha, df)
  
    # calculate the p-value
    p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
    
    # Return everything
    return t_stat, df, cv, p


#------------------------------------------------------------------------------
# Calculate the t test
#------------------------------------------------------------------------------

# Data
seed(1)

# Generate the 1st sample
data1 = 5 * randn(100) + 50

# Create dependent sample
data2 = 2 * data1 + 3
    
alpha = 0.05

t_stat, df, cv, p = dependent_T_test(data1, data2, alpha)
print('t = %.3f, df = %d, cv = %.3f, p = %.3f' % (t_stat, df, cv, p))

# Interpret via critical value
if abs(t_stat) <= cv:
    print('(t <= critical value) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(t >  critical value) ==> REJECT the H0 that the means are equal.')

# Interpret via p-value
if p > alpha:
    print('(p >  alpha) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(p <= alpha) ==> REJECT the H0 that the means are equal.')
    

'''----------------------------------------------------------------------------
   Cách 2: Sử dụng Sử dụng scipy.stats import ttest_rel             
----------------------------------------------------------------------------'''

t_stat, p = ttest_rel(data1, data2)
print('\nt = %.3f, p = %.3f' % (t_stat, p))

# Interpret via p-value
if p > alpha:
    print('(p >  alpha) ==> ACCEPT the H0 that the means are equal.')
else:
    print('(p <= alpha) ==> REJECT the H0 that the means are equal.')
