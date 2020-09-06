"""=============================================================================
Bài toán 1: Một nhà sản xuất đang điều tra tuổi thọ hoạt động của pin laptop
          máy tính xách tay (life_batteries.txt).
   1. Tạo life_array từ nội dung tập tin.
   2. Vẽ biểu đồ phân phối tần suất của life_array
   3. Làm bảng phân phối tần suất cho dữ liệu theo các khoảng:
         120-129, 130-139, 140-149, 150-159, 160 - 169.
   4. Vẽ biểu đồ khối cho bảng phân phối tần suất trên. 
      Biểu đồ câu 2 và câu 4 nói lên điều gì?
   5. Thống kê cơ bản cho life_array; 
      mean, median, mode (những giá trị nào? số lần bao nhiêu?), max, min, ...
   6. Tìm độ nhọn, độ xiên của dữ liệu. Nhận xét kết quả
   -----------------------------------------------------------------------------
   Bổ sung sau khi học bài 6:
   7. Nếu số lượng mẫu nhỏ hơn 150, hãy cho biết xác suất các mẫu nhỏ hơn 150. 
      Nhận xét.
   8. Tìm xác suất của P(140 ≤ X ≤ 155). Nhận xét
============================================================================="""
import numpy             as np
import matplotlib.pyplot as plt
import pandas            as pd
import seaborn           as sns

from numpy import mean, median
from scipy import stats

print('====================================================')
print('*** 1. Tạo mảng dữ liệu chứa từ nội dung tập tin ***')
print('====================================================')
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 5/'
f          = open(folder + 'life_batteries.txt', 'r')

content    = f.read()
f.close()
print('Data:\n', content, '\n')

life       = content.split()
life       = list(map(int, life))
life_array = np.array(life)
print('Life array:\n', type(life_array), '(', life_array.size, ')\n', life_array, '\n')

print('=======================================================')
print('*** 2. Vẽ biểu đồ phân phối tần suất của dữ liệu    ***')
print('=======================================================')
plt.figure(figsize = (8, 4))
plt.subplot(1, 2, 1)
plt.hist(life_array)
plt.subplot(1, 2, 2)
sns.distplot(life_array)
plt.show()

print('========================================================')
print('*** 3. Vẽ histogram cho các khoảng:                  ***')
print('***    120-129, 130-139, 140-149, 150-159, 160-169.  ***')
print('========================================================')
freq = pd.Series()
freq['120-129'] = np.extract((life_array >= 120) & (life_array <= 129), life_array).size
freq['130-139'] = np.extract((life_array >= 130) & (life_array <= 139), life_array).size
freq['140-149'] = np.extract((life_array >= 140) & (life_array <= 149), life_array).size
freq['150-159'] = np.extract((life_array >= 150) & (life_array <= 159), life_array).size
freq['160-169'] = np.extract((life_array >= 160) & (life_array <= 169), life_array).size
print('Bảng phân phối tần suất:\n', freq)

print('=======================================================')
print('*** 4. Vẽ biểu đồ khối và nhận xét                  ***')
print('=======================================================')
plt.bar(freq.index, freq)

''' Nhận xét:
    Hầu hết dữ liệu tập trung trong khoảng 130-139, với một vài điểm vượt quá 150.
    Có thể kết luận: trung tâm của dữ liệu là một điểm nào đó trong khoảng 130-139.
    Từ 2 biểu đồ trên, có thể xác định nhiều biện pháp phân tán và xu hướng trung tâm:???
'''

print('================================================')
print('*** 5. Những thống kê cơ bản trên dữ liệu  y ***')
print('================================================')
print('Mean   x_    =', mean(life_array))
print('MIN    x_min =', min(life_array))
print('MAX    x_max =', max(life_array))
print('Median x_med =', median(life_array))

x_mod = stats.mode(life_array)
print('Mode   x_mod =', x_mod[0][0])
print('       f(x)  =', x_mod[1][0]) # số lần freq.

range_life = np.ptp(life_array)
print('Range        =', range_life)

var_life = np.var(life_array)
print('Variance     =', var_life)

std_life = np.std(life_array)
print('Std-dev.     =', std_life)

## Vẽ box plot --> không có outlier

## Ngắt breakpoint tại đây
## Chạy tiếp tục mới cho kết quả đúng (?!) 
sns.boxplot(life_array)


print('=================================================')
print('*** 6. Tìm độ nhọn, độ xiên. Nhận xét kết quả ***')
print('=================================================')
# 
skew_life = stats.skew(life_array)
print('Skewness     =', skew_life) # > 0: phân phối lệch PHẢI

kur_life = stats.kurtosis(life_array) # fisher = True (default) --> (kur - 3)
print('Kurtosis     =', kur_life)

kur_life = stats.kurtosis(life_array, fisher = False)
print('Kurtosis     =', kur_life) # < 0: THẤP hơn phân phối chuẩn

## Có thể sử dụng stats.describe()
print('Số liệu thống kê:', stats.describe(life_array))

print('=================================================')
print('*** 7. Tìm xác suất các mẫu nhỏ hơn 150       ***')
print('=================================================')
p_x_150 = np.extract(life_array < 150, life_array).size/life_array.size
print('Pr(x < 150)    =', p_x_150) 
# Nhận xét: Có thể 90% pin sẽ bị hỏng trước 150 phút

#   8. Tìm xác suất của P(140 ≤ X ≤ 155). Nhận xét
p_x_140 = np.extract(life_array >= 140, life_array).size/life_array.size
p_x_155 = np.extract(life_array >  155, life_array).size/life_array.size
print('Pr([140, 155]) =', p_x_140 - p_x_155) 
# Nhận xét: Có thể 30% pin sẽ có tuổi thọ kéo dài từ 140 phút đến 155 phút.


"""=============================================================================
Bài toán 2: Xem xét một bộ dữ liệu 40 mẫu của một nhãn hiệu pin khác (Battery 2).
    Các quan sát được liệt kê trong tập tin life_batteries_2.txt.
   1. Tạo life2_array từ nội dung tập tin.
   2. So sánh 2 nhóm pin ở bài toán 1 và ở bài toán 2 theo histogram và nhận xét
   3. Làm bảng phân phối tần suất cho dữ liệu theo các khoảng:
         120-129, 130-139, 140-149, 150-159, 160 - 169.
   4. Vẽ biểu đồ khối cho bảng phân phối tần suất trên. 
      Biểu đồ câu 2 và câu 4 nói lên điều gì?
   5. So sánh hai nhóm mẫu dựa trên thống kê chung (dùng stats.describe(array))
      Nhận xét kết quả.
   6. Tạo dataframe chứa tần suất của cả 2 nhóm mẫu gồm có 2 cột là batteries_1 
      và batteries_2, index là các khoảng như câu 3
   7. Vẽ boxplot cho cả 2 nhóm batteries_1 và batteries_2 => nhận xét
============================================================================="""

## 1. Tạo life2_array từ nội dung tập tin.
f2       = open(folder + '/life_batteries_2.txt', 'r')
content2 = f2.read()
f2.close()
print('Data:\n', content2, '\n')

life2 = content2.split()
life2 = list(map(int, life2))
life2_array = np.array(life2)
print('Life array 2:\n', type(life2_array), '(', life2_array.size, ')\n', life2_array, '\n')

## 2. So sánh 2 nhóm pin ở bài toán 1 và ở bài toán 2 theo histogram và nhận xét
plt.figure(figsize = (8, 4))
plt.subplot(1, 2, 1)
plt.hist(life_array)
plt.title('Battery group 1')
plt.subplot(1, 2, 2)
plt.hist(life2_array)
plt.title('Battery group 2')
plt.show()

plt.figure(figsize = (8, 4))
plt.subplot(1, 2, 1)
sns.distplot(life_array)
plt.title('Battery group 1')
plt.subplot(1, 2, 2)
sns.distplot(life2_array)
plt.title('Battery group 2')
plt.show()
''' Nhận xét:
    Có nhiều dữ liệu hơn cho Battery 2 trong khoảng 140 so với Battery 1 trong khoảng 130.
    Ngoài ra, mức độ biến thiên của Battery 2 ít hơn so với Battery 1.
    Dựa trên các kết quả này, có thể kết luận rằng Battery 2 là một nhãn hiệu tốt hơn 
    (trung bình cao hơn và biến thiên thấp hơn). 
    Tuy nhiên, tính hợp lệ của kết luận này còn phụ thuộc vào cách thu thập dữ liệu.
'''

## 3. Làm bảng phân phối tần suất cho dữ liệu theo các khoảng:
##         120-129, 130-139, 140-149, 150-159, 160-169.
freq2 = pd.Series()
freq2['120-129'] = np.extract((life2_array >= 120) & (life2_array <= 129), life2_array).size
freq2['130-139'] = np.extract((life2_array >= 130) & (life2_array <= 139), life2_array).size
freq2['140-149'] = np.extract((life2_array >= 140) & (life2_array <= 149), life2_array).size
freq2['150-159'] = np.extract((life2_array >= 150) & (life2_array <= 159), life2_array).size
freq2['160-169'] = np.extract((life2_array >= 160) & (life2_array <= 169), life2_array).size
print('Bảng phân phối tần suất:\n', freq2)

## 4. Vẽ biểu đồ khối cho bảng phân phối tần suất trên. 
##      Biểu đồ câu 2 và câu 4 nói lên điều gì?
plt.bar(freq2.index, freq2)

## 5. So sánh hai nhóm mẫu dựa trên thống kê chung (dùng stats.describe(array))
##      Nhận xét kết quả.
freq_df = pd.DataFrame({'Batteries 1':freq, 'Batteries 2':freq2})
print('Bảng phân phối tần suất chung:\n', freq_df)

print('Số liệu thống kê Battery 1:', stats.describe(life_array))
print('Số liệu thống kê Battery 2:', stats.describe(life2_array))
''' Nhận xét:
       - Battery 2 có tuổi thọ trung bình cao hơn và phương sai nhỏ hơn.
       - Battery 1 có skewness > 0: phân phối lệch phải
       - Battery 2 có skewness < 0: phân phối lệch trái
       - Battery 1 có kurtosis < 0: phân bố này thấp hơn phân bố chuẩn
       - Battery 2 có kurtosis > 0: phân bố này cao hơn phân bố chuẩn
'''

## 6. Tạo dataframe chứa tần suất của cả 2 nhóm mẫu gồm có 2 cột là batteries_1 
##    và batteries_2, index là các khoảng như câu 3
df = pd.DataFrame({'Batteries 1':life_array, 'Batteries 2':life2_array})
print('Số liệu thống kê:\n', df.describe())
print(df.info())

## Trộn 2 tập dữ liệu ?
dd = pd.melt(df, value_vars = ['Batteries 1', 'Batteries 2'], var_name = 'batteries')
print(dd.head())

## Ngắt breakpoint tại đây
## Chạy tiếp tục mới cho kết quả đúng (?!) 
## 7. Vẽ boxplot cho cả 2 nhóm batteries_1 và batteries_2 => nhận xét
sns.boxplot(y = 'batteries', x = 'value', data = dd, hue = 'batteries', whis = 'range')

''' Nhận xét:
    - Nhóm Pin 1 không có outliers, nhóm Pin 2 có outliers (?)
    - Phân phối Pin 2 tập trung hơn phân phối Battery 1
    - Phạm vi của Battery 2 ngắn hơn so với Battery 1 (ít thay đổi hơn) 
      và được chuyển sang bên phải (trung tâm cao hơn).
'''



