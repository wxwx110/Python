#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09oopClassDef2.py
@Time    :   2019/07/20 21:28:17
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
class Father(object):
    def __init__(self):
        print('Father__init__')
        print('father init: self',self)
    
    def __new__(cls):
        print ("Father__new__")
        t= object.__new__(cls)
        print('Father__new__ t',t)
        return t

    def funcFather(self):
        print('funcFather')


class Son(Father):
    def __init__(self):
        print('Son __init__')
        print('Son init: self',self)
    
    def __new__(cls):
        print ("Son __new__")
        t= object.__new__(cls)
        print('Son __new__ t',t)
        return t
    
a=Son()

a.funcFather()

