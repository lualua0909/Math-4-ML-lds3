"""=============================================================================
   Ex6: Gradient Descent - SAT
   Case study: "SAT and College GPA" của 105 SV vào học chuyên ngành CS
               ở một trường công lập địa phương. 
               Chúng ta cần dự đoán university GPA nếu biết high school GPA.
      1) Đọc dữ liệu trên vào dataframe
      2) Trực quan hóa dữ liệu theo high school GPA, university GPA
         Ta có: x = high school GPA (định dạng chuẩn), y = university GPA
      3) Với phương trình: y = mx + b (univ_GPA = (m * high_GPA) + b) 
            gọi hàm tính m, b: theta = gradient_descent_2(alpha, x, y, 1000)
      4) Từ m, b (m = theta[1], b = theta[0]) => dự đoán univ_GPA theo m, b
      5) Trực quan hóa dữ liệu
      6) Dự đoán univ_GPA lần lượt với high_GPA là 2.3, 2.8, 3.3, 3.8   
============================================================================="""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import os, sys
LDS3folder = 'D:/NAT/RnD/Edu/01.CD - DH/T3H.LDS3.Maths and Stats for Data Science'
folder     = LDS3folder + '/Materials/Projects/B4. Calculus'
lib_path = os.path.abspath(os.path.join(folder))
sys.path.append(lib_path)
import chapter4_lib as lib

##------------------------------------------------------------------------------
## 1) Đọc dữ liệu trên vào dataframe
##------------------------------------------------------------------------------
folder = LDS3folder + '/Materials/Projects/Data/Bai 4/'
data   = pd.read_excel(folder + "sat.xls")

high_GPA = data.high_GPA.values
print('Ma trận High GPD', high_GPA.shape, high_GPA[0:3])

univ_GPA = data.univ_GPA.values
print('Ma trận Univ GPD', univ_GPA.shape, univ_GPA[0:3])

##------------------------------------------------------------------------------
## 2) Trực quan hóa dữ liệu theo high_GPA, univ_GPA
##------------------------------------------------------------------------------
plt.figure(figsize = (12, 12))
sns.jointplot(x = 'high_GPA', y = 'univ_GPA', data = data)
plt.show()
      
## 3) Với phương trình: y = mx + b (univ_GPA = (m * high_GPA) + b) 
##       gọi hàm tính m (slope), b (theta/bias)
##------------------------------------------------------------------------------
print('-------------- Cách 1: Giải bằng hàm tính Gradient descent ------------')
##------------------------------------------------------------------------------
## Thêm 1 cột chứa giá trị 1 vào cột đầu tiên của x --> xBar
M     = high_GPA.size
xBar1 = np.c_[np.ones(M), high_GPA] # insert column
y     = univ_GPA
alpha = 0.01 # learning rate
theta = lib.gradient_descent_2(alpha, xBar1, y, 1000)

print('Ma trận x', xBar1.shape)
print('Ma trận y', y.shape)

slope1 = theta[1]
bias1  = theta[0]

##------------------------------------------------------------------------------
## 4) Dự đoán univ_GPA theo m (slope), b (bias)
##------------------------------------------------------------------------------
for i in range(xBar1.shape[1]):
    univ_GPA_predict = (slope1 * xBar1) + bias1

##------------------------------------------------------------------------------
## 5) Trực quan hóa dữ liệu
##------------------------------------------------------------------------------
print('\n y = m.x + B --> y = ', slope1, '.x + (', bias1, ')\n')
plt.figure(figsize = (12, 8))
plt.xlim(2.0, 4.0)
plt.ylim(2.0, 4.0)
plt.scatter(xBar1[:, 1], univ_GPA, color = "blue")
plt.plot(xBar1, univ_GPA_predict)
plt.xlabel("High School GPA")
plt.ylabel("University GPA")
plt.show()

##------------------------------------------------------------------------------
## 6) Dự đoán univ_GPA lần lượt cho GPA là 2.3, 2.8, 3.3, 3.8
##------------------------------------------------------------------------------
high_GPA_new = np.array([2.3, 2.8, 3.3, 3.8])
univ_GPA_new = (slope1 * high_GPA_new) + bias1
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[0])
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[1])
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[2])
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[3])



"""----------------------------------------------------------------------------
## Giải phương trình: A.w = b bằng công thức dựa trên ma trận giả nghịch đảo:
   Ký hiệu:
      - Vô hướng: slope (w1), bias (w0) 
      - Ma trận : x(m, n)
                  y(m, 1)
                  xBar(m, n + 1)
                  A(n + 1, n + 1) = Xbar_T.Xbar
                  b(n + 1, 1)     = Xbar_T.y
                  w(n + 1, 1)     = pseudoInverse(A).b
-----------------------------------------------------------------------------"""
print('\n---- Cách 2: Giải bằng công thức dựa trên ma trận giả nghịch đảo ----')

print('Ma trận High GPD', high_GPA.shape, high_GPA[0:3])
x = np.zeros((high_GPA.size, 1))
x[:, 0] = high_GPA
print('Ma trận x', x.shape, x[0:3])

print('Ma trận University GPD', univ_GPA.shape, univ_GPA[0:3])
y = np.zeros((univ_GPA.size, 1))
y[:, 0] = univ_GPA
print('Vectơ   y', y.shape, y[0:3])

## Thêm 1 cột chứa giá trị 1 vào cột đầu tiên của x --> xBar
one   = np.ones((x.shape[0], 1))
xBar2 = np.concatenate((one, x), axis = 1)
print('Ma trận xBar', xBar2.shape, xBar2[0:3])

A = np.dot(xBar2.T, xBar2)
print('Ma trận A', A.shape, A)

b = np.dot(xBar2.T, y)
print('Ma trận b', b.shape, b)

w = np.dot(np.linalg.pinv(A), b)
print('Vector chứa các tham số w', w.shape, w)

slope2 = w[1] 
bias2  = w[0]   

##------------------------------------------------------------------------------
## 5) Trực quan hóa dữ liệu
##------------------------------------------------------------------------------
print('\ny = m.x + B --> y = ', slope2, '.x + (', bias2, ')\n')
for i in range(xBar2.shape[1]):
    y_predict = (slope2 * xBar2) + bias2

plt.figure(figsize = (12, 8))
plt.xlim(2.0, 4.0)
plt.ylim(2.0, 4.0)
plt.scatter(xBar2[:, 1], univ_GPA, color = "green")
plt.plot(xBar2, y_predict)
plt.xlabel("High School GPA")
plt.ylabel("University GPA")
plt.show()

##------------------------------------------------------------------------------
## 6) Dự đoán univ_GPA lần lượt cho GPA là 2.3, 2.8, 3.3, 3.8
##------------------------------------------------------------------------------
high_GPA_new = np.array([2.3, 2.8, 3.3, 3.8])
univ_GPA_new = (slope2 * high_GPA_new) + bias2
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[0])
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[1])
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[2])
print(u'Dự đoán High school GPA 2.3 có University GPA: %.2f' %univ_GPA_new[3])

print('--------------- Cách 3: Giải bằng thư viện scikit-learn ---------------')
from sklearn import linear_model

## fit_intercept = False for calculating the bias
regr = linear_model.LinearRegression(fit_intercept = False) 
regr.fit(xBar2, y)

## So sánh 2 cách giải
print('Sử dụng scikit-learn:', regr.coef_)
print('Sử dụng công thức   :', w.T)
