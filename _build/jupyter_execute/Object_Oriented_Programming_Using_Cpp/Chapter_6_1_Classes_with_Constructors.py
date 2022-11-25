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
# # Classes with Constructors

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates classes with constructors in C++

# ```c++
# /*********************************************************************
# 
#   Filename:  modulo.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.1    Classes with Constructors
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //Modulo numbers and constructor initialization
# 
# #include  <iostream>
# 
# using namespace std;
# 
# const int  modulus = 60;
# 
# // Modulo numbers and constructor initialization
# class  mod_int {
# public:
#    mod_int(int i);     //constructor declaration
#    void  assign(int i) { v = i % modulus; }
#    void  print() const { cout << v << '\t'; }
#    const static int modulus = 60;
# private:
#    int  v;
# };
# 
# inline  mod_int::mod_int(int i = 0)
# {
#     v = i % modulus;
# }
# const int  mod_int::modulus;
# 
# int main()
# {
#    int      seconds = 400;
#    mod_int  z(seconds);
# 
#    cout << seconds << " seconds equals "
#         << seconds / 60 << " minutes ";
#    z.print();
#    cout << " seconds" << endl;
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_1_Classes_with_Constructors"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ modulo.cpp -w -o modulo")


# In[5]:


exec_status = os.system("./modulo")


# In[ ]:




