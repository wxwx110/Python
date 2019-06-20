#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14oopProperty2.py
@Time    :   2019/06/20 15:32:24
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# property 讲函数的方法封装成属性调用
class Student(object):

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
    
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    #只读属性
    @property
    def age(self):
        return 2015 - self._birth

a=Student()
# 如果没有@property需要这样调用
#a.score(89)
a.score=89
a.birth=1981
print (a.score)
print (a.age)




