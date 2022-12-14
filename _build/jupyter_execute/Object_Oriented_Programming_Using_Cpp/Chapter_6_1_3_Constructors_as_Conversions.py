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
# # Constructors as Conversions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates conversions with constructors in C++

# ```c++
# /*********************************************************************
# 
#   Filename:  printabl.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.1    Constructors as Conversions
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# // Adapted for g++ by Mark Khusid
# 
# // ASCII Printable characters
# 
# #include <iostream>        // changed iostream.h to iostream MK
# 
# using namespace std;       // Added by MK
# 
# class  pr_char {
# public:
#    pr_char(int i = 0) : c(i % 128) {}
#    void   print() const { cout << rep[c]; }
# private:
#    int           c;
#    static const char*  rep[128];
# };
# 
# const char*  pr_char::rep[128] = {
#      "nul", "soh", "stx", "etx", "eot", "enq", "ack", "bel", "bs",  "ht",
#      "nl",  "vt",  "np",  "cr",  "so",  "si",  "dle", "dc1", "dc2", "dc3",
#      "dc4", "nak", "syn", "etb",  "can", "em", "sub", "esc", "fs",  "gs",
#      "rs", "us", "sp", "!", "\"", "#", "$", "%", "&", "'",
#      "(", ")", "*", "+", ",", "-", ".", "/", "0", "1",
#      "2", "3", "4", "5", "6", "7", "8", "9", ":", ";",
#      "<", "=", ">", "?", "@", "A", "B", "C", "D", "E",
#      "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
#      "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
#      "Z", "[", "|", "]", "^", "_", "'", "a", "b", "c"
#      "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
#      "x", "y", "z", "{", "|", "}", "~", "del"};
# 
# int main()
# {
#    pr_char  c;
# 
#    for (int i = 0; i < 128; ++i) {
#       c = i;  //or: c = static_cast<pr_char>(i);
#       c.print();
#       cout << endl;
#    }
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_1_3_Constructors_as_Conversions"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ printabl.cpp -w -o printabl")


# ## Execution Process

# In[5]:


exec_status = os.system("./printabl")


# In[ ]:




