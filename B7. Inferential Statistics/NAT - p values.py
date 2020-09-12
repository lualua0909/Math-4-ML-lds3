"""============================================================================
   Hàm tính p-value từ giá trị t-statistics:
      * t_stat: giá trị t-statistics
      * df    : bậc tự do
============================================================================"""
def t2p(t_stat, df):
   import scipy.stats as stats
   p_value = (1 - stats.t.cdf(abs(t_stat), df)) * 2
   return p_value
#------------------------------------------------------------------------------
   
t_stat  = [2.613, 2.611]
df      = 39
 
for t in t_stat:
   p_value = t2p(t, df)
   print('   * t_stat = %.5f' %t, '--> p-value = %.5f' %p_value)
