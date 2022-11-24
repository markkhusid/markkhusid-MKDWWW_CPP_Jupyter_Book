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
# # An Example:  Dynamically Allocated Strings

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison- Wesley)

# ## Program that demonstrates dynamically allocated strings using classes in C++

# ```c++
# //An implementation of dynamically allocated strings.
# #include <iostream>
# #include <string.h>
# #include <assert.h>
# 
# using namespace std;
# 
# class my_string {
# public:
#     my_string() : len(0) {
#         s = new char[1];
#         assert (s != 0);
#         s[0] - 0;
#     }
# 
#     my_string(const my_string& str);    // copy constructor
#     
#     my_string(const char* p);           // conversion constructor
#     
#     ~my_string () {
#         delete []s;
#     }
# 
#     void assign(const my_string& str);
# 
#     void print() const {
#         cout << s << endl;
#     }
# 
#     void concat(const my_string& a, const my_string& b);
# 
# private:
#     char* s;
#     int len;
# };
# 
# my_string::my_string(const char* p)
# {
#     len = strlen(p);
#     s = new char[len +1];
#     assert (s != 0);
#     strcpy(s, p);
# }
# 
# my_string::my_string(const my_string& str) : len(str.len)
# {
#     s = new char[len + 1];
#     assert(s != 0);
#     strcpy(s, str.s);
# }
# 
# void my_string::assign(const my_string& str)
# {
#     if (this == &str)       // a = a; do nothing
#         return;
#     delete []s;
#     len = str.len;
#     s = new char[len + 1];
#     assert(s != 0);
#     strcpy(s, str.s);
# }
# 
# void my_string::concat(const my_string& a, const my_string& b)
# {
#     char* temp = new char[a.len + b.len + 1];
#     len = a.len + b.len;
#     strcpy(temp, a.s);
#     strcat(temp, b.s);
#     delete []s;
#     s = new char[len + 1];
#     assert(s != 0);
#     strcpy(s, temp);
# }
# 
# int main()
# {
#     char* str = "The wheel that squeaks the loudest\n";
#     my_string a(str), b, author("Josh Billings\n"), both, quote;
# 
#     b.assign("Is the one that gets the grease\n");
#     both.concat(a, b);
#     quote.concat(both, author);
#     quote.print();
# }
# ```

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_4_An_Example__Dynamically_Allocated_Strings"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ string5.cpp -w -o string5")


# In[5]:


exec_status = os.system("./string5")

