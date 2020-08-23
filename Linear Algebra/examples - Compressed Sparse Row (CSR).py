'''============================================================================
Minh họa: Matrix --> Compressed Sparse Row (CSR format): row oriented
   (Xem ví dụ bên dưới)
   Giả sử ma trận A có m dòng và A có p phần từ <> 0
   
   ** Tạo 3 arrays có kích thước khác nhau:
      1) data[p]      : chứa các giá trị <> 0
      2) indices[p]   : chứa các chỉ số CỘT của các phần tử <> 0
      3) indptr[m + 1]: chứa một dãy số tăng (không đều) từ 0 cho đến p
                        là VỊ TRÍ BẮT ĐẦU rút trích trong data[] cho mỗi dòng
         idxptr = (start_r(0), start_r(1), start_r(2), ..., start_r(m-1), p)
         
         Lưu ý: indptr[0]     = start_r(0) = 0
                idxptr[m + 1] = p
                
         VD: idxptr = (0, 2, 5, 7, 9, 12)
         
         Gọi P(i) là tập các giá trị <> 0 của dòng i, rút trích từ trong data[]
         P(0) = { data[0], data[1] }
         P(1) = { data[2], data[3], data[4] }
         P(2) = { data[5], data[6] }
         P(3) = { data[7], data[8] }
         P(4) = { data[9], data[10], data[11] }
============================================================================'''
import numpy as np
import scipy.sparse as sparse

A = np.array([[8, 0, 0, 6, 0, 0], 
              [0, 0, 9, 0, 0, 4],
              [0, 0, 0, 3, 0, 0]])

# Matrix --> CSR format    
csr = sparse.csr_matrix(A)

# DATA array:     [8 6 9 4 3]
print('DATA    array: ', csr.data)

# INDICES array:  [0 3 2 5 3]
print('INDICES array: ', csr.indices)

''' Các bước tạo nên mảng INDPTR[] có (m + 1 = 4) phần tử (ma trận A có 3 dòng)
      * INDPTR[] = [0 ? ? 5] vì A có p = 5 phần tử <> 0 và INDPTR[0] luôn luôn = 0

      * Dòng i = 1 có phần tử <> 0 đầu tiên là 9, tương ứng với phần tử data[2]
                   cho nên idxptr[i = 1] = 2
                    --> INDPTR[] = [0 2 ? 5]
      * Dòng i = 2 có phần tử <> 0 đầu tiên là 3, tương ứng với phần tử data[4]
                   cho nên idxptr[i = 2] = 4
                    --> INDPTR[] = [0 2 4 5]
'''
print('INDPTR  array: ', csr.indptr)


'''----------------------------------------------------------------------------
Minh họa: CSR format --> matrix
   http://scipy-lectures.org/advanced/scipy_sparse/csr_matrix.html
----------------------------------------------------------------------------'''
d   = np.array([8, 6, 9, 4, 3])
ind = np.array([0, 3, 2, 5, 3])
ptr = np.array([0, 2, 4, 5])
mtx = sparse.csr_matrix((d, ind, ptr))
print('\nTái tạo ma trận từ CSR format (default shape):\n', mtx.todense())
'''   * ptr[] có 4 phần tử ==> ma trận có 3 dòng
      * ptr[0] = 0
        ptr[1] = 2
        ptr[2] = 4
        ptr[3] = 5 ==> ma trận có 5 phần tử khác 0 lưu trữ trong d[]
        
      * P(0): lấy từ chỉ số ptr[0] = 0, nghĩa là từ d[0], cho đến d[1]
              vì d[2] là chỉ số bắt đầu của P(1)
              P(0) = {d[0], d[1]} = {8, 6}
                 d[0] --> indices[0] = 0 --> A(0, 0) = 8
                 d[1] --> indices[1] = 3 --> A(0, 3) = 6
              
      * P(1): lấy từ chỉ số ptr[1] = 2, nghĩa là từ d[2], cho đến d[3]
              vì d[4] là chỉ số bắt đầu của P(2)
              P(1) = {d[2], d[3]} = {9, 4}
                 d[2] --> indices[2] = 2 --> A(1, 2) = 9
                 d[3] --> indices[3] = 5 --> A(1, 5) = 4
              
      * P(2): lấy từ chỉ số ptr[2] = 4, nghĩa là từ d[4], cho đến hết
              vì là dòng cuối cùng của ma trận
                 d[4] --> indices[4] = 3 --> A(2, 3) = 3

        [8 0 0 6 0 0]
        [0 0 9 0 0 4]
        [0 0 0 3 0 0]
'''

mtx = sparse.csr_matrix((d, ind, ptr), shape = (3, 9))
print('Tái tạo ma trận từ CSR format (explicite shape):\n', mtx.todense())



