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
# # Chapter 6.11: No Constructor, Copy Constructor, and Other Mysteries

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates an implicit copy constructor in C++

# In file tracking.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  tracking.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.11   No Constructor, Copy Constructor Other Mysteries
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# #include  <iostream>
# 
# using namespace std;
# 
# // personal data tracking
# 
# struct pers_data {
#    int   age;           //in years
#    int   weight;        //in kilograms
#    int   height;        //in centimeters
#    char  name[20];      //last name
# };
# 
# void print(pers_data d)
# {
#    cout << d.name << " is " << d.age
#         << " years old\n";
#    cout << "weight : " << d.weight << "kg,  height : "
#         << d.height << "cm." << endl;
# }
# 
# int main()
# {
#    pers_data  laura = {3, 14, 88, "POHL"};
#                   //construction off the stack
# 
#    print(laura);  //calls copy constructor
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_11_No_Constructor_Copy_Constructor_and_Other_Mysteries"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ tracking.cpp -w -o tracking")


# ## Execution Process

# In[5]:


exec_status = os.system("./tracking")

