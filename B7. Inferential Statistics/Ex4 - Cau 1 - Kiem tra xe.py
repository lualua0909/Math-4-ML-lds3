"""============================================================================
   Sở GTCC muốn kiểm tra sự an toàn của các xe nhỏ, hạng trung và cỡ lớn. 
    1. Tạo dataframe như hình vẽ.
    2. Vẽ boxplot, quan sát kết quả.
    3. Áp dụng ANOVA để xem có sự khác biệt đáng kể giữa 3 loại xe (alpha = 5%).
============================================================================"""
# Load packages
import pandas            as pd
import matplotlib.pyplot as plt
import scipy.stats       as stats
import seaborn           as sns
import statsmodels.api   as sm

from statsmodels.formula.api     import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 1. Tạo dataframe 
df = pd.DataFrame({'S_cars': [643, 655, 702],
                   'M_cars': [469, 427, 525],
                   'X_cars': [484, 456, 402]})

# 2. Vẽ boxplot, quan sát kết quả.
sns.boxplot(data=df)
plt.show()

 # 3. Áp dụng ANOVA
fvalue, pvalue = stats.f_oneway(df.S_cars, df.M_cars, df.X_cars)
print(fvalue, pvalue)

# get ANOVA table as R like output
# reshape the d dataframe suitable for statsmodels package
df_melt = pd.melt(df.reset_index(), id_vars = ['index'], 
                  value_vars = ['S_cars', 'M_cars', 'X_cars'])

# replace column names
df_melt.columns = ['index', 'cars', 'value']

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(cars)', data = df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ = 2)
print(anova_table)

# Giá trị P-value có ý nghĩa về mặt thống kê (P < 0.05),
# do đó, có thể kết luận rằng có sự khác biệt đáng kể giữa các loại xe.

# perform multiple pairwise comparison (Tukey HSD)
m_comp = pairwise_tukeyhsd(endog = df_melt['value'], groups = df_melt['cars'], alpha = 0.05)
print(m_comp)

# ngoại trừ X_cars và M_cars, tất cả các so sánh cặp khác đều bác bỏ H0
# và chỉ ra sự khác biệt đáng kể về mặt thống kê.

# Kiểm định Levene: phương sai bằng nhau ?
w, pvalue = stats.levene(df.S_cars, df.M_cars, df.X_cars)
print(w, pvalue)
# p-value > 0.05 => không bác bỏ H0: các mẫu từ các quần thể có phương sai bằng nhau.

# Kiểm định phân phối chuẩn
w, pvalue = stats.shapiro(model.resid)
print(w, pvalue)

# p-value > 0.05 => không bác bỏ H0: dữ liệu được rút ra từ phân phối chuẩn.

