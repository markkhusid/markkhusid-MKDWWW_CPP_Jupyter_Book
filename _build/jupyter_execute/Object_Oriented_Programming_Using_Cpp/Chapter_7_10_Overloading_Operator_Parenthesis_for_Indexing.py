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
# # Chapter 7.10: Overloading Operator () for Indexing

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates overloading the function call operator () for use in matrix indexing in C++

# In file matrix3.cpp

# ```{literalinclude} Cpp_Code/Chapter_7_10_Overloading_Operator_Parenthesis_for_Indexing/matrix3.cpp
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


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_7_10_Overloading_Operator_Parenthesis_for_Indexing"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ matrix3.cpp -w -o matrix3")


# ## Execution Process

# In[5]:


exec_status = os.system("./matrix3")

