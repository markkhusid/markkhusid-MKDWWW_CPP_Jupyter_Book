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
# # Chapter 7.1: ADT Conversions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates an implicit copy constructor in C++

# In file string7.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  string7.cpp
#   Chapter:   7      Ad Hoc Polymorphism
#   Section:   7.1    ADT Conversions
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# // An implementation of dynamically allocated strings.
# // with conversions and overloaded assignment
# 
# #include <iostream>
# #include <string.h>
# #include <assert.h>
# 
# using namespace std;
# 
# class my_string {
# public:
#    my_string() : len(0)
#       { 
#          s = new char[1];
#          assert(s != 0); 
#          s[0] = 0;
#       }
#    my_string(const my_string& str); //copy constructor
#    my_string(const char* p);        //conversion constructor
#    ~my_string() 
#       { 
#          delete []s; 
#       }
#    void print() const 
#       { 
#          cout << s << endl; 
#       }
#    // Had to make the parameter const so that the program can compile.  MK.   
#    my_string operator=(const my_string& a);
#    operator char*();     //conversion to char*
# private:
#    char*  s;
#    int    len;
# };
# 
# // No return type.  MK.
# my_string::operator char*()
# {
#    char*  p = new char[len + 1];
#    assert(p != 0);
#    strcpy(p, s);
#    return p;
# }
# 
# my_string::my_string(const char* p)
# {
#    len = strlen(p);
#    s = new char[len + 1];
#    assert(s != 0);
#    strcpy(s, p);
# }
# 
# my_string::my_string(const my_string& str) : len(str.len)
# {
#    s = new char[len + 1];
#    assert(s != 0);
#    strcpy(s, str.s);
# }
# 
# // Had to make the parameter const so that the program can compile.  MK.
# my_string my_string::operator=(const my_string& a)
# {
#    if (this != &a) {       //a = a; do nothing
#       if (a.len != len) {  //  if need different size string
#          delete []s;
#          len = a.len;
#          s = new char[len + 1];
#          assert(s != 0);
#       }
#       strcpy(s, a.s);
#    }
#    return *this;
# }
# 
# int main()
# {
#    my_string s("Test it"), c("One"), d("Two");
#    char* logo = "Geometrics Inc";
#    char* logo2 = "MK Dynamics Inc";
#    char* testit;
# 
#    testit = s;
#    cout << testit << endl;     // check convert my_string to char*
#    s = "One two three";
#    s.print();
#    s = logo;                   // check convert char* to my_string and =
#    s.print();
#    s = static_cast<my_string>(logo2);
#    s.print();
#    c = s = d;                  //check multiple assign on overloaded =
#    c.print();
#    s.print();
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_7_1_ADT_Conversions"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ string7.cpp -w -o string7")


# ## Execution Process

# In[5]:


exec_status = os.system("./string7")

