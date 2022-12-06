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
# # Chapter 6.7: An Example: A Singly Linked List

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates a singly linked list using classes in C++

# In file slist.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  slist.cpp
#   Chapter:   6      Object Creation and Destruction
#   Section:   6.7    An Example:  A Singly Linked List
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# //A singly linked list
# 
# #include <iostream>         // Changed iostream.h to iostream. MK.
# #include <assert.h>
# 
# using namespace std;       // Added. MK.
# 
# struct slistelem {
#    char       data;
#    slistelem*  next;
# };
# 
# class slist { //a singly linked list
# public:
#    slist() : h(0) { };        //0 denotes empty slist
#    ~slist();                  // alternative { release(); }
#    void  prepend(char c);     //adds to front of slist
#    void  del();
#    slistelem*  first() const { return h; };
#    void  print() const;
#    void  release();
# private:
#    slistelem*  h;           //head of slist
# };
# 
# 
# void slist::prepend(char c)
# {
#    slistelem*  temp = new slistelem;//create element
#    assert(temp != 0);
#    temp -> next = h;                //link to slist
#    temp -> data = c;
#    h = temp;                 //update head of slist
# }
# 
# void slist::del()
# {
#    slistelem*  temp = h;
# 
#    h = h -> next;     //presumes an non-empty slist
#    delete temp;
# }
# 
# void slist::print() const   //object is unchanged
# {
#    slistelem*  temp = h;
# 
#    while (temp != 0) {     //detect end of slist
#       cout << temp -> data << " -> ";
#       temp = temp -> next;
#    }
#    cout << "\n###" << endl;
# }
# 
# //elements returned to free store
# void slist::release()
# {
#    while (h != 0)
#       del();
# }
# 
# slist:: ~slist()
# {
#    cout << "destructor invoked" << endl;
#    release();
# }
# 
# int main()
# {
#    slist*  p;
#    {
#       slist  w;
# 
#       w.prepend('A');
#       w.prepend('B');
#       w.print();
#       w.del();
#       w.print();
#       p = &w;
#       p -> print();
#       cout << "exiting inner block" << endl;
#    }
#    //p -> print();  gives system dependent behavior
#    cout << "exiting outer block" << endl;
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_6_7_An_Example__A_Singly_Linked_List"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ slist.cpp -w -o slist")


# ## Execution Process

# In[5]:


exec_status = os.system("./slist")

