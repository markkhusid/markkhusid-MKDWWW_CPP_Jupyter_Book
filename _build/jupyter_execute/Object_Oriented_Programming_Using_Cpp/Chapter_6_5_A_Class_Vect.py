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
# # A Class Vect

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates a dynamic array or vector in C++

# In file vect1.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  vect1.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.7    A Class vect
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //test of safe array type vect
# 
# #include "vect1.h"
# 
# using namespace std;    // Added. MK
# 
# int main()
# {
#    vect a(60), b[20];
# 
#    b[1].element(5) = 7;
#    cout << b[1].element(5) << " 1 element 5\n";
#    for (int i = 0; i <= a.ub(); ++i) {
#       a.element(i) = i;
#       cout << a.element(i) << "\t";
#    }
#    cout << endl;     // Added for output clarity
# }
# ```

# In file vect1.h

# ```C++
# /*********************************************************************
# 
#   Filename:  vect1.h
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.5    A class vect
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //Implementation of a safe array type vect
# 
# #include  <iostream>    // changed iostream.h to iostream. MK
# #include  <assert.h>
# 
# //Implementation of a safe array type vect
# class vect {
# public:
#    explicit vect(int n = 10);
#    ~vect() { delete []p; }
#    int&  element(int i);                 //access p[i]
#    int  ub() const {return (size - 1);}  //upper bound
# private:
#    int*  p;
#    int   size;
# };
# 
# vect::vect(int n) : size(n)
# {
#    assert(n > 0);
#    p = new int[size];
#    assert(p != 0);
# }
# 
# int& vect::element(int i)
# {
#    assert (i >= 0 && i < size);
#    return p[i];
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_5_A_Class_Vect"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ vect1.cpp -w -o vect1")


# ## Execution Process

# In[5]:


exec_status = os.system("./vect1")

