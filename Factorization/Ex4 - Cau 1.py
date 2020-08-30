"""=============================================================================
   Ex4: SVD Demensionality Reduction
   Câu 1: 
      a) Cho tập tin iris.csv, đọc dữ liệu ra dataframe và chỉ lấy 4 cột đầu
      b) Phân tích SVD: U, s, VT từ dataframe, 
      c) Giảm chiều còn 2 components
      d) Trực quan hóa dữ liệu sau khi giảm chiều, có luôn cột 5 (species) 
============================================================================="""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/Data/Bai 2/'

## a) Đọc tập tin iris vào dataframe
iris = pd.read_csv(folder + 'iris2.csv')
print('\n*** a) Dataframe iris.csv:')
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
print('         - Ma trận iris', iris.shape, ':')
print('                    ', iris.head())
print('         - Ma trận X', X.shape, ':')
print('         - 4 cột đầu tiên:\n', X.head())

## b) Phân tích SVD: U, s, VT
U, s, VT = np.linalg.svd(X)

print('\n*** b) Phân tích SVD:')
print('         - Ma trận U', U.shape, ':\n', U)
print('         - Eigenvalues:', s)
print('         - Ma trận VT', VT.shape, ':\n', VT)

## c) Giảm chiều còn 2 components
if (X.shape[0] == X.shape[1]):
    S = np.diag(s)
else:
    S = np.zeros_like(X)
    S[:X.shape[1], :X.shape[1]] = np.diag(s)

print('\n*** c) NEW dataframe (using only the first two components):')
## Chỉ sử dụng 2 components: S(n,  2); VT(2, n)
n_components = 2
S  =  S[:, :n_components]
VT = VT[:n_components, :]

## d) Trực quan hóa dữ liệu sau khi giảm chiều, có luôn cột 5 (species)
##    - Cột thứ 5 (species) chứa các giá trị: setosa, versicolor, virginica
## T_s1 = U.S = U.S.VT.V = X.V = T_s2
T_s1 = U.dot(S)
T_s1[0:5]

T_s2 = X.dot(VT.T)
T_s2[0:5]

## Visualization
## T_s2 có 2 columns, đặt tên là comp1, comp2
T_s2.columns = ["comp1", "comp2"]
## Bổ sung cột [iris.species] vào T_s2 --> T_s2(comp1, comp2, species)
T_s2["species"] = iris['species']

print('         - U.S', T_s2.shape, ': \n', U)
T_s2.head()

plt.figure(figsize = (8, 8))
plt.scatter(T_s2["comp1"], T_s2["comp2"])
plt.show()

plt.figure(figsize=(8, 8))
sns.scatterplot(x = "comp1", y = "comp2", data = T_s2, hue = "species")
plt.show()
