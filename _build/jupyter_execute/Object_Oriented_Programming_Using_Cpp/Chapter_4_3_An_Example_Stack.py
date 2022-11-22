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
# # An Example Stack

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates an example stack data structure in C++

# ch1_stac1.cpp

# ```c++
# // Test of ch_stack by reversing a string.
# #include "ch_stac1.h"
# #include <iostream>
# 
# using namespace std;
# 
# int main()
# {
#     ch_stack s;
#     char str[40] = {"My name is Betty Dolsberry!"};
#     int i = 0;
# 
#     cout << str << endl;
#     reset(&s);
#     while (str[i] && !full(&s))
#         push (&s, str[i++]);
#     while (!empty(&s))
#         cout << pop(&s);
#     cout << endl;
# }
# ```

# ch_stac1.h

# ```c++
# // A simple implementation of type ch_stack
# 
# const int max_len = 1000;
# enum { EMPTY = -1, FULL = max_len -1 };
# 
# struct ch_stack
# {
#     char s[max_len];
#     int top;
# };
# 
# // A standard set of ch_stack operations.
# 
# void reset(ch_stack * stk)
# {
#     stk -> top = EMPTY;
# }
# 
# void push(ch_stack * stk, char c)
# {
#     stk -> s[++stk -> top] = c;  
# }
# 
# char pop(ch_stack * stk)
# {
#     return (stk -> s[stk -> top--]);
# }
# 
# char top(ch_stack * stk)
# {
#     return (stk -> s[stk -> top]);
# }
# 
# bool empty(const ch_stack * stk)
# {
#     return (stk -> top == EMPTY); 
# }
# 
# bool full(const ch_stack * stk)
# {
#     return (stk -> top == FULL);
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" + "Cpp_Code/Chapter_4_3_An_Example_Stack"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ ch_stac1.cpp -w -o ch_stac1")


# In[5]:


exec_status = os.system("./ch_stac1")

