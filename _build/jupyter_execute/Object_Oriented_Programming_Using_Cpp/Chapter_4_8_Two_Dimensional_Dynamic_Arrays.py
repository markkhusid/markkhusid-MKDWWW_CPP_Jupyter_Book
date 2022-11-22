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
# # Two Dimensional Dynamic Arrays

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates dynamic arracy creation, manipulation and destruction in C++

# ```c++
# // Dynamic arrays in two dimensions
# #include <iostream>
# using namespace std;
# 
# struct twod {
#     double **   base;
#     int         row_size, column_size;
# };
# 
# void allocate (int r, int s, twod & m)
# {
#     m.base = new double * [s];
#     for (int i = 0; i < s; ++i)
#         m.base[i] = new double[r];
#     m.row_size = r;
#     m.column_size = s;
# }
# 
# void deallocate(twod & m)
# {
#     for (int i = 0; i < m.column_size; ++i)
#         delete [] m.base[i];
#     delete [] m.base;
#     m.row_size = 0;
#     m.column_size = 0;
# }
# 
# double find_max(const twod & m)
# {
#     int i, j;
#     double max = m.base[0][0];
# 
#     for (i = 0; i < m.column_size; ++i)
#         for (j = 0; j < m.row_size; ++j)
#             if (m.base[i][j] > max)
#                 max = m.base[i][j];
#     return (max);
# }
# 
# int main ()
# {
#     twod    a, b;
#     int     i, j;
# 
#     allocate(2, 3, a);
#     allocate(4, 6, b);
# 
#     for (i = 0; i < a.column_size; ++i)
#         for (j = 0; j < b.row_size; ++j)
#             a.base[i][j] = i * j;
#     
#     for (i = 0; i < b.column_size; ++i)
#         for (j = 0; j < b.row_size; ++j)
#             b.base[i][j] = i * j;
# 
#     cout << find_max(a) << " max in size 2 * 3\n";
#     cout << find_max(b) << " max in size 4 * 6\n";
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_4_8_Two_Dimensional_Dynamic_Arrays"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ array_2d.cpp -w -o array_2d")


# In[5]:


exec_status = os.system("./array_2d")

