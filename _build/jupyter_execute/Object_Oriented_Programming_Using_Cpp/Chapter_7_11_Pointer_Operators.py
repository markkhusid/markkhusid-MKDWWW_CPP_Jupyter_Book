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
# # Chapter 7.11: Pointer Operators

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates overloading the pointer operator -> in C++

# In file triple.cpp

# ```{literalinclude} Cpp_Code/Chapter_7_11_Pointer_Operators/triple.cpp
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


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_7_11_Pointer_Operators"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ triple.cpp -w -o triple")


# ## Execution Process

# In[5]:


exec_status = os.system("./triple")

