#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np


# In[2]:


def create_matrix(m, n):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            s= "M[" + str(i+1) + "," + str(j+1) + "]:"
            x = eval(input(s))
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)


# In[3]:


def create_vector(n):
    lst = []
    for i in range(n):
        s= "v[" + str(i+1) + "]:"
        x = eval(input(s))
        lst.append(x)
    return np.array(lst)


# In[4]:


def create_matrix_random(m, n, start, end):
    lst = []
    for i in range(m):
        lst_sub = []
        for j in range(n):
            x = random.randint(start,end+1)
            lst_sub.append(x)
        lst.append(lst_sub)
    return np.array(lst)


# In[5]:


def create_vector_random(n, start, end):
    lst = []
    for i in range(n):        
        x = random.randint(start,end+1)
        lst.append(x)
    return np.array(lst)


# In[ ]:




