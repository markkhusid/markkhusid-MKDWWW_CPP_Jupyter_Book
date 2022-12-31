#!/usr/bin/env python
# coding: utf-8
---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# # Chapter 7.7: Overloading Assignment and Subscripting Operators

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates overloading assignment and subscripting operators in C++

# In file vect2.cpp

# ```{literalinclude} Cpp_Code/Chapter_7_7_Overloading_Assignment_and_Subscripting_Operators/vect2.cpp
# ---
# language: C++
# ---
# ```

# In file vect2.h

# ```{literalinclude} Cpp_Code/Chapter_7_7_Overloading_Assignment_and_Subscripting_Operators/vect2.h
# ---
# language: C++
# ---
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_7_7_Overloading_Assignment_and_Subscripting_Operators"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ vect2.cpp -w -o vect2")


# ## Execution Process

# In[5]:


exec_status = os.system("./vect2")


# In[ ]:




