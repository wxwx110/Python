#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12oopProperty.py
@Time    :   2019/06/18 16:37:45
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

class Student(object):
    #定义类属性
    name = 'TTT'

s=Student()
#再没有定义实例属性的情况下回去寻找类属性
print(s.name)
print(Student.name)
# 增加类属性
s.name="tom"
print(s.name)
print(Student.name)

#删除实例属性
del s.name 
print(s.name)
print(Student.name)

class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

