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
# # Chapter 6.10: Strings Using Reference Semantics

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates using linked lists to store strings with a reference counter in C++

# In file string6.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  string6.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.10   Strings Using Reference Semantics
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //Reference counted my_strings
# #include  <iostream>
# #include  <assert.h>
# #include  <cstring>
# 
# using namespace std;
# 
# class str_obj {
# public:
#    int    len, ref_cnt;
#    char*  s;
#    str_obj() : len(0), ref_cnt(1)
#       { s = new char[1]; assert(s != 0); s[0] = 0; }
#    str_obj(const char* p) : ref_cnt(1)
#       { len = strlen(p); s = new char[len + 1];
#         assert(s != 0); strcpy(s, p); }
#    ~str_obj() { delete []s; }
# };
# 
# class my_string {
# public:
#    my_string() { st = new str_obj; assert(st != 0);}
#    my_string(const char* p)
#       { st = new str_obj(p); assert(st != 0);}
#    my_string(const my_string& str)
#        { st = str.st; st -> ref_cnt++; }
#    ~my_string();
#    void  assign(const my_string& str);
#    void  print() const { cout << st -> s; }
# private:
#    str_obj*  st;
# };
# 
# void my_string::assign(const my_string& str)
# {
#    if (str.st != st) {
#       if (--st -> ref_cnt == 0)
#          delete st;
#       st = str.st;
#       st -> ref_cnt++;
#    }
# }
# 
# my_string:: ~my_string()
# {
#    if (--st -> ref_cnt == 0)
#       delete st;
# }
# 
# int main()
# {
#    char*   str = "The wheel that squeaks the loudest\n";
#    my_string  a(str), b ;
# 
#    b.assign("Is the one that gets the grease\n");
#    cout << str << endl;
#    a.print();
#    b.print();
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_10_Strings_Using_Reference_Semantics"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ string6.cpp -w -o string6")


# ## Execution Process

# In[5]:


exec_status = os.system("./string6")

