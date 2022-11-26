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
# # The Copy Constructor

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates a copy constructor in C++

# In file ch_stac4.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  ch_stac4.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.2    Constructing a Dynamically Sized Stack
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //Stack implementation with constructor
# 
# #include <iostream>        // Changed iostream.h to iostream. MK
# #include "ch_stac4.h"
# 
# 
# using namespace std;       // Added. MK
# 
# int cnt_char(char c, ch_stack s)
# {
#    int  count = 0;
# 
#    while (!s.empty())
#       count += (c == s.pop());
#    return count;
# }
# 
# int main()
# {
#    ch_stack  typea(100);    //size only
#    ch_stack  typeb;         //no size
#    ch_stack  typec(50, "My name is Ira Pohl!\n");  //size and initializer
#    ch_stack  typed(typec);
#    char reverseline[200];
#    char a [30] = {"My name is Laura Pohl!\n"};
#    char b [40] = {"My name is Debra Dolsberry!\n"};
#    int  i = 0;
# 
#    cout << "\nNumber of a's in typec shoud be 2. It is "
#         << cnt_char('a', typec) << endl;
# 
#    typea.reset();
# 
#    while (a[i])
#       if (!typea.full())
#     typea.push(a[i++]);
# 
#    i = 0;
#    while (!typea.empty())
#       reverseline[i++] = typea.pop();
#    reverseline[i] = '\0';
#    cout << reverseline;
# 
#    i = 0;
#    while (b[i])
#       if (!typeb.full())
#     typeb.push(b[i++]);
# 
#    i = 0;
#    while (!typeb.empty())
#       reverseline[i++] = typeb.pop();
#    reverseline[i] = '\0';
#    cout << reverseline;
# 
#    i = 0;
#    while (!typec.empty())
#       reverseline[i++] = typec.pop();
#    reverseline[i] = '\0';
#    cout << reverseline;
#    i = 0;
# 
#    while (!typed.empty())
#       reverseline[i++] = typed.pop();
#    reverseline[i] = '\0';
#    cout << reverseline;
# }
# ```

# In file ch_stac4.h

# ```C++
# /*********************************************************************
# 
#   Filename:  ch_stac4.h
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.2    Constructing a Dynamically Sized Stack
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //Stack implementation with constructor
# 
# #include <iostream>         // Changed iostream.h to iostream
# #include <assert.h>
# #include <cstring>         // Added for memcpy. MK
# 
# //ch_stack implementation with constructor.
# class ch_stack {
# public:
# //the public interface for the ADT ch_stack
#    explicit ch_stack(int size):
#       max_len( size), top(EMPTY)
#    { assert(size > 0);s = new char[size]; assert(s != 0);}
#    ch_stack();
#    ch_stack(const ch_stack& str);
#    ch_stack(int size, const char str[]);
#   ~ch_stack() { delete []s; }   //destructor
#    void  reset() { top = EMPTY; }
#    void  push(char c) { s[++top]= c; }
#    char  pop() { return s[top--]; }
#    char  top_of() const { return s[top]; }
#    bool  empty() const { return (top == EMPTY); }
#    bool  full() const { return (top == max_len - 1); }
# private:
#    enum  { EMPTY = -1 };
#    char*  s;              //changed from s[max_len]
#    int    max_len;
#    int    top;
# };
# 
# //default constructor for ch_stack
# ch_stack::ch_stack():max_len(100),top(EMPTY)
# {
#    s = new char[100];
#    assert(s != 0);
# }
# 
# //domain transfer
# ch_stack::ch_stack(int size, const char str[]):
#    max_len(size)
# {
#    int i;
#    assert(size > 0);
#    s = new char[size];
#    assert(s != 0);
#    for (i = 0; i < max_len && str[i] != 0; ++i)
#       s[i] = str[i];
#    top = --i;
# }
# 
# //Copy constructor for ch_stack of characters
# ch_stack::ch_stack(const ch_stack& str):
#    max_len(str.max_len),top(str.top)
# {
#    s = new char[str.max_len];
#    assert(s != 0);
#    memcpy(s, str.s, max_len);
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_2_1_The_Copy_Constructor"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ ch_stac4.cpp -w -o ch_stac4")


# ## Execution Process

# In[5]:


exec_status = os.system("./ch_stac4")

