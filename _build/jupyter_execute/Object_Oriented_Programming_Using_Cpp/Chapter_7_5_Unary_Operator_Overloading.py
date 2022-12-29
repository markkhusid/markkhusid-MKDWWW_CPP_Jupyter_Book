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
# # Chapter 7.5: Unary Operator Overloading

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates unary operator overloading in C++

# In file clock.cpp:

# ```{literalinclude} Cpp_Code/Chapter_7_5_Unary_Operator_Overloading/clock.cpp
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


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_7_5_Unary_Operator_Overloading"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ clock.cpp -w -o clock")


# ## Execution Process

# In[5]:


exec_status = os.system("./clock")

