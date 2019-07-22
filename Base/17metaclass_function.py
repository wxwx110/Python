#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   17metaclassFunction.py
@Time    :   2019/07/22 10:00:47
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

def printName(self):
    print(self.name)
@classmethod
def funclassmethod(cls):
    print(cls.name)
@staticmethod
def staticlassmethod(type):
    print(type.name)
# 创建类时，添加函数和属性
test=type('Test',(),{'name':'Tom', 'printName':printName,'funClassmethod':funclassmethod,'staticClassmethod':staticlassmethod})
test().printName()
# help(test)
test.funClassmethod()
test.staticClassmethod(test)


