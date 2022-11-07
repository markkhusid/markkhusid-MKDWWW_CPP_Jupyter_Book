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
# # The C++ Standard Template Library

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates use of the C++ Standard Template Library

# ```c++
# // Using the list container.
# #include <iostream>
# #include <list>
# #include <numeric>
# using namespace std;
# 
# void print(const list<double> &lst)
# { // using an iterator to traverse lst
#     list<double>::const_iterator where;
# 
#     for(where = lst.begin(); where != lst.end(); ++where)
#         cout << *where << '\t';
#     cout << endl;
# }
# 
# int main()
# {
#     double w[4] = {0.9, 0.8, 88, -99.99};
#     list<double> z;
# 
#     for (int i = 0; i < 4; ++i)
#         z.push_front(w[i]);
#     print(z);
#     z.sort();
#     print(z);
#     cout << "sum is " << accumulate(z.begin(), z.end(), 0.0) << endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Colletion (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_1_7_The_Standard_Template_Library"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ stl_list.cpp -w -o stl_list")


# In[5]:


exec_status = os.system("./stl_list")

