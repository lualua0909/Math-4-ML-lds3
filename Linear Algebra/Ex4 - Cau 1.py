# -*- coding: utf-8 -*-
"""============================================================================
   Ex4: MATRICES & VECTORS - Câu 1
       2a +  b +  c = 4
        a + 3b + 2c = 5
        a           = 6
       Quy về Ax = B. Sau đó giải tìm x 
============================================================================"""

import numpy as np

A = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]])
print('A     =', A)

B = np.array([4, 5, 6])
print('B     =', B)

print("Nghiệm [a, b, c] =", np.linalg.solve(A, B))