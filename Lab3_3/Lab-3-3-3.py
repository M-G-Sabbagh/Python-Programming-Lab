#!/usr/bin/env python
# coding: utf-8

# In[3]:


f= open("python_lab.txt","w+")
f.write("N F\n")
f.close()
with open('python_lab.txt', 'a') as file: #calls file.close automatically
    file.write("97")

