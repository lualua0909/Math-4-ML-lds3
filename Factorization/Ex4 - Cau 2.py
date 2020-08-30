"""=============================================================================
   Ex4: SVD Demensionality Reduction
   Câu 2: 
      a) Tải dữ liệu digits từ dataset của sklearn
      b) Sử dụng TruncatedSVD để giảm chiều dữ liệu xuống 10 components
      c) Trực quan hóa dữ liệu sau khi giảm chiều
https://chrisalbon.com/machine_learning/feature_engineering/dimensionality_reduction_on_sparse_feature_matrix/
============================================================================="""

from sklearn.decomposition import TruncatedSVD
from scipy.sparse import csr_matrix
from sklearn import datasets

## a) Tải dữ liệu digits từ dataset của sklearn
digits = datasets.load_digits()
print('         - Matrix X', digits.data.shape, ': \n', digits.data, '\n')

## Standardize the feature matrix
X = digits.data

## Make sparse matrix
X_sparse = csr_matrix(X)
print('         - Sparse matrix', X_sparse.shape, ': \n', X_sparse, '\n')

## b) Phân tích Truncated SVD với k = 10: U, s, VT
tsvd = TruncatedSVD(n_components = 10)

## Conduct TSVD on sparse matrix
X_sparse_tsvd = tsvd.fit(X_sparse).transform(X_sparse)

## Show results
print('Original number of features:', X_sparse.shape[1])
print('Reduced  number of features:', X_sparse_tsvd.shape[1])

print('         - X[0]: \n', X[0], '\n')
print('         - X[0]: \n', X_sparse_tsvd[0], '\n')

## View Percent Of Variance Explained By New Features
# Sum of 10 components' explained variance ratios
tsvd.explained_variance_ratio_[0:10].sum()

## 73% with 10 components