#!/usr/bin/env python
# coding: utf-8

# section 2-4:
# 
# 1) a = [1, 2, 4, ..., 2^16]
# 
# 2) b = [1, 4, 9, 4^2]
# 
# 3) c = [a[4], a[16]] = [16, 2^16]

# In[6]:


a = [2**i for i in range(17)]
print(a)
b = [x*x for x in range(1,5)]
print(b)
c = [a[x] for x in b if x % 2 == 0]
print(c)

