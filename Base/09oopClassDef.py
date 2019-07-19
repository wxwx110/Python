#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09oopBase.py
@Time    :   2019/06/18 09:20:51
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
class Student(object):

    def __init__(self,name,age):
        self.name=name
        #增加两个下划线后不能在类的外部访问
        self.__age=age

        
    # 类中方法的第一个参数必须是self
    def getName(self):
        return self.name
    def getAge(self):
        return self.__age

a=Student("tom",20)
b=Student("jerry",20)

print(a.getName())
print(b.getAge())

print(a.name)
# age增加下划线不能直接访问
#print(a.__age)
# python编译器修改了改属性的名称 _类名+属性名，不同版本的解释器，可能会不同
print(a._Student__age)