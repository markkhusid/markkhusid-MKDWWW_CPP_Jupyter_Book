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
# # Chapter 7.3: Friend Functions

# Adapted from: "Object-Oriented Programming Using C++" by Ira Pohl (Addison - Wesley)

# ## Program that demonstrates friend functions selection in C++

# In file vect2.h

# ```c++
# /*********************************************************************
# 
#   Filename:  vect2.h
#   Chapter:   7      Ad Hoc Polymorphism
#   Section:   7.7    Friend Functions
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# class matrix;                 // forward reference
# 
# #include  <iostream>         // Changed iostream.h to iostream. MK.
# #include  <assert.h>
# 
# using namespace std;          // Added. MK.
# 
# class vect {
# public:
#    vect() { size = 10; p = new int[size]; }
#    explicit vect(int n);
#    vect(const vect& v);
#    vect(const int a[], int n);  //initialize by array
#    ~vect() { delete []p; }
#    int  ub() const { return (size - 1); }  //upper bound
#    vect& operator=(const vect& v);  //overload assignment
#    void print() const;
#    int&  operator[](int i) ;         //range checked
#    vect operator+(const vect& v);
# private:
#    int*  p;
#    int   size;
#    friend vect mpy(const vect& v, const matrix& m);
# };
# 
# vect::vect(int n) : size(n)
# {
#    assert(n > 0);
#    p = new int[size];
#    assert(p != 0);
# }
# 
# vect::vect(const int a[], int n) : size(n)
# {
#    assert(n > 0);
#    p = new int[size];
#    assert(p != 0);
#    for (int i = 0; i < size; ++i)
#       p[i] = a[i];
# }
# 
# vect::vect(const vect& v) : size(v.size)
# {
#    p = new int[size];
#    assert(p != 0);
#    for (int i = 0; i < size; ++i)
#       p[i] = v.p[i];
# }
# 
# int& vect::operator[](int i)
# {
#    assert(i >= 0 && i < size);
#    return p[i];
# }
# 
# vect& vect::operator=(const vect& v)
# {
#    int s = (size < v.size) ? size : v.size;
# 
#    if (v.size != size)
#       cerr << "copying different size arrays "
#            << size << " and " << v.size << endl;
#    for (int i = 0; i < s; ++i)
#       p[i] = v.p[i];
#    return (*this);
# }
# 
# 
# void vect::print() const
# {
#    for (int i = 0; i <= (size-1); ++i)
#       cout << p[i] << "\t";
#    cout << endl;
# }
# 
# vect vect::operator+(const vect& v)
# {
#    assert(size == v.size);
#    vect  sum(size);
#    for (int i = 0; i < size; ++i)
#       sum.p[i] = p[i] + v.p[i];
#    return sum;
# }
# ```

# In file matrix2.cpp

# ```c++
# /*********************************************************************
# 
#   Filename:  matrix2.cpp
#   Chapter:   7      Ad Hoc Polymorphism
#   Section:   7.3    Friend Functions
#   Compiler:  Borland C++     Version 5.0       Summer 1996
#   Object Oriented Programming Using C++, Edition 2   By Ira Pohl
# 
# *********************************************************************/
# 
# class matrix;                 // forward reference
# 
# #include  <iostream>        // Changed iostream.h to iostream. MK.
# #include  <assert.h>
# #include  "vect2.h"
# 
# using namespace std;          // Added. MK.
# 
# class matrix {
# public:
#    matrix(int d1, int d2);
#    ~matrix();
#    int  ub1() const { return(s1 - 1); }
#    int  ub2() const { return(s2 - 1); }
#    void print() const;
#    int&  element(int i, int j);
# private:
#    int**  p;
#    int    s1, s2;
#    friend    vect mpy(const vect& v, const matrix& m);
# };
# 
# matrix::matrix(int d1, int d2) : s1(d1), s2(d2)
# {
#    assert (d1 > 0 && d2 > 0);
#    p = new int*[s1];
#    assert(p != 0);
#    for (int i = 0; i < s1; ++i)
#       p[i] = new int[s2];
# }
# 
# matrix::~matrix()
# {
#    for (int i = 0; i <= ub1(); ++i)
#       delete p[i];
#    delete []p;
# }
# 
# int& matrix::element(int i, int j)
# {
#    assert(i >= 0 || i <= ub1() || j >= 0 || j <= ub2());
#    return p[i][j];
# }
# 
# 
# vect mpy(const vect& v, const matrix& m)
# {
#    assert(v.size == m.s1);    //check sizes
#    //use privileged access to p in both classes
#    vect  ans(m.s2);
#    int   i, j;
# 
#    for (i = 0; i <= m.ub2(); ++i) {
#       ans.p[i] = 0;
#       for (j = 0; j <= m.ub1(); ++j)
#          ans.p[i] += v.p[j] * m.p[j][i];
#    }
#    return ans;
# }
# 
# void matrix::print() const
# {
#    int j;
#    for (int i = 0; i <= ub1(); ++i) {
#       cout << "\nrow  " << (i + 1) << endl;
#       for (j = 0; j <= ub2(); ++j)
#          cout << p[i][j] << "\t";
#    }
#    cout << endl;
# }
# 
# 
# void init_vect(vect& v, int start, int incr)
# {
#    for (int i = 0; i <= v.ub(); ++i) {
#       v[i] = start;
#       start += incr;
#    }
# }
# 
# int main()
# {
#    vect   a(3), b(3), c(6), d(6);
#    matrix m(3, 6) ;
#    int    i, j;
# 
#    a[0] = 1 + (a[1] = 1 + ( a[2] = 1)) ;
#    init_vect(b, 1, 1);
#    init_vect(c, 10, 10);
#    init_vect(d, 100, 1);
# 
#    cout << "vector a is\n";
#    a.print();
#    cout << "\nvector b is\n";
#    b.print();
#    cout << "\nvector c is\n";
#    c.print();
#    cout << "\nvector d is\n";
#    d.print();
# 
#    for (i = 0; i <= m.ub1(); ++i)
#       for (j = 0; j <= m.ub2(); ++j)
#          m.element(i, j) = i + j;
# 
#    cout << "\nmatrix m is\n";
#    m.print();
# 
#    c = mpy(a, m);
#    cout << "\nvector c product is\n";
#    c.print();
# }
# ```

# ## Compilation Process

# The above program is compiled and run using Gnu Compiler Collection (g++):

# In[1]:


import os
root_dir = os.getcwd()


# In[2]:


code_dir = root_dir + "/" +     "Cpp_Code/Chapter_7_3_Friend_Functions"


# In[3]:


os.chdir(code_dir)


# In[4]:


build_command = os.system("g++ matrix2.cpp -w -o matrix2")


# ## Execution Process

# In[5]:


exec_status = os.system("./matrix2")

