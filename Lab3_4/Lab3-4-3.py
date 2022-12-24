#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
mat = np.random.randint(0, 2, (5,5))
print(mat)
# mat = np.array([[1, 0, 0, 0, 1],[0, 0, 0, 0, 0],[0, 0, 1, 0, 0]])

indices_y = np.array([[x for x in range(mat.shape[1])] for y in range(mat.shape[0])])
indices_x = np.array([[x for y in range(mat.shape[1])] for x in range(mat.shape[0])])

[x,y] = np.where(mat==1)
sumsum = np.zeros(mat.shape)
for i in range(np.sum(mat)):
    sumsum = sumsum + np.abs(indices_x-x[i]) + np.abs(indices_y-y[i])
[c_x,c_y] = np.where(sumsum == np.min(sumsum))
print(c_x[0],c_y[0])


# # brute force implementation
# sumsum = np.zeros(mat.shape)
# n = np.nonzero(mat)
# print(mat)
# for i in range(mat.shape[0]):
#     for j in range(mat.shape[1]):
#         sumsum[i,j] = np.sum(abs(n[0]-i))+np.sum(abs(n[1]-j))
# print(np.where(sumsum==np.amin(sumsum)))


