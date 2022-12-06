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
# # Chapter 6.6: Members that Are Class Types 

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates class members that are class types in C++

# In file vect1.h

# ```c++
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
# #include  <iostream>                      // changed iostream.h to iostream. MK.
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

# In file pairvect.cpp

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
# #include  <iostream>                      // changed iostream.h to iostream. MK.
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


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_6_Members_that_Are_Class_Types"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ pairvect.cpp -w -o pairvect")


# ## Execution Process

# In[5]:


exec_status = os.system("./pairvect")

