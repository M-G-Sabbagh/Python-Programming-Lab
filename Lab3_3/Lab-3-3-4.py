#!/usr/bin/env python
# coding: utf-8

# In[14]:


from os import path
from os import mkdir
from os import getcwd
if not path.exists("input_files"):
    mkdir("input_files")
else:
    print("Directory alreay exists")
current_path = path.abspath(getcwd())
f = open(current_path+"\\input_files\\python_lab.txt","w+")
f.write("N F\n")
f.close()

