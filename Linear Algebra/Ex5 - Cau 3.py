# -*- coding: utf-8 -*-
"""=============================================================================
    Ex5: SPARSE MATRIX - Câu 3
        a) Tạo ma trận thưa thớt ngẫu nhiên S(5,5) với mật độ density = 0.25
        b) Chuyển S thành full matrix A
        c) Tạo ma trận thưa thớt ngẫu nhiên S1(5,5) với mật độ density = 0.25 
           và item khác 0 sẽ bằng 1
        d) Chuyển S1 thành full matrix A1
        e) Trực quan hóa S, S1
============================================================================="""
import scipy.sparse as sparse
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

## a) create sparse matrix with density 0.25
np.random.seed(42)      # set random seed to repeat

S = sparse.random(5, 5, density = 0.25)
print(S)

## b) Convert the sparse matrix to a full matrix
A = S.toarray()
print("Sử dụng toarray: ", A)

plt.spy(S)

# create sparse matrix with density 0.25
# link: https://cmdlinetips.com/2019/02/how-to-create-random-sparse-matrix-of-specific-density/
""" Ngầm định, các giá trị sẽ được tạo theo uniform distribution trong [0, 1)
    Tham số data_rvs dùng để chỉ định phân phối cho các giá trị được tạo ra     
"""
""" Trường hợp 1: Chỉ lấy giá trị (nhị phân) trong tập hợp {0, 1}
"""
S1 = sparse.random(5, 5, density = 0.25, data_rvs = np.ones)
print(S1)

A1 = S1.toarray()
plt.spy(S1)

""" Trường hợp 2: Normal distribution
                  Mean = 3 và Standard deviation = 1 
"""
rvs = stats.norm(loc = 3, scale = 1).rvs
S1 = sparse.random(5, 5, density = 0.25, data_rvs = rvs)
print("Normal distribution: ", S1)

A1 = S1.toarray()
plt.spy(S1)
 
""" Trường hợp 3: Poisson distribution
                  Mean = 10 
"""
rvs = stats.poisson(15, loc = 10).rvs
S1 = sparse.random(5, 5, density = 0.25, data_rvs = rvs)
print("Poisson distribution: ", S1)

A1 = S1.toarray()
plt.spy(S1)
 