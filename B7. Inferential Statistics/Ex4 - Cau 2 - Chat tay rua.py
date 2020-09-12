"""============================================================================
   1. Cho tập tin data.xlsx. Đọc dữ liệu
   2. Dữ liệu có 2 factors: Detergent (super, best), Temperature (hot, warm, cold).
   3. Sử dụng ANOVA hai chiều, đánh giá chất tẩy rửa và nhiệt độ ảnh hưởng 
      như thế nào đối với chất bẩn bị loại bỏ.
      a) Ảnh hưởng của chất tẩy rửa đến lượng chất bẩn bị loại bỏ 
      b) Ảnh hưởng của nhiệt độ đến lượng chất bẩn bị loại bỏ 
      c) Ảnh hưởng của chất tẩy rửa và nhiệt độ đến lượng chất bẩn bị loại bỏ
      H0D: Lượng chất bẩn bị loại bỏ không phụ thuộc vào loại chất tẩy rửa.
      H0T: Lượng chất bẩn bị loại bỏ không phụ thuộc vào nhiệt độ.
============================================================================"""
import pandas            as pd
import matplotlib.pyplot as plt
import scipy.stats       as stats
import seaborn           as sns
import statsmodels.api   as sm

from statsmodels.formula.api     import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 1. Load data file
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 7/'
data       = pd.read_excel(folder + 'data.xlsx')
print(data)

# reshape the d dataframe suitable for statsmodels package
# you do not need to reshape if your data is already in stacked format.
# Compare d and d_melt tables for detail understanding
d_melt = pd.melt(data, id_vars = ['type'], value_vars = ['cold', 'warm', 'hot'])
# replace column names
d_melt.columns = ['type', 'temperature', 'value']
d_melt.head()

# 2. Vẽ boxplot, quan sát kết quả.
plt.figure(figsize = (12,10))
sns.boxplot(x = "type", y = "value", hue = "temperature", data = d_melt, palette = "Set3")
plt.show()

 # 3. Áp dụng ANOVA
model = ols('value ~ C(type) + C(temperature) + C(type):C(temperature)', data = d_melt).fit()
anova_table = sm.stats.anova_lm(model, typ = 2)
print(anova_table)

# Sự khác biệt về chất tẩy rửa và nhiệt độ có ý nghĩa thống kê,
# nhưng ANOVA không cho biết chất tẩy rửa và nhiệt độ khác nhau đáng kể với nhau. 
# Để biết các cặp chất tẩy rửa và nhiệt độ khác nhau đáng kể, 
# thực hiện nhiều phân tích so sánh cặp bằng cách sử dụng Tukey HSD test.

# perform multiple pairwise comparison (Tukey HSD)
m_comp = pairwise_tukeyhsd(endog = d_melt['value'], groups = d_melt['type'], alpha=0.05)
print(m_comp)

# ngoại trừ X_cars và M_cars, tất cả các so sánh cặp khác đều bác bỏ H0
# và chỉ ra sự khác biệt đáng kể về mặt thống kê.

# Kiểm định Levene: phương sai bằng nhau ?
w, pvalue = stats.levene(data['hot'], data['warm'], data['cold'])
print(w, pvalue)
# p-value > 0.05 => không bác bỏ H0: các mẫu từ các quần thể có phương sai bằng nhau.

for name, grouped_df in d_melt.groupby('type'):
    print('type: {}'.format(name), pairwise_tukeyhsd(grouped_df['value'], 
                                                     grouped_df['temperature'], 
                                                     alpha = 0.05))
