#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   13oop__slots__.py
@Time    :   2019/06/18 20:40:40
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
class Student(object):
    pass

a=Student()
#给实例添加属性在实例创建之后
a.name="tom"
print(getattr(a,"name"))
# 给实例添加方法
from types import MethodType
def setName(self ,name):
    self.name=name
a.setName= MethodType(setName, a) # 给实例绑定一个方法
a.setName("Jerry")
print(getattr(a,"name"))
# 以上方法绑定的实例只能给绑定实例使用，其他对象不能使用
b=Student()
# print(b.name) #报错

#给类，动态添加属性和方法
Student.className='class1'
Student.getClass=lambda self:self.className

print(a.getClass())
print(b.getClass())

class Student2(object):
    # 用tuple定义允许绑定的属性名称
    # 仅对当前类对象有效，对继承类对象无效
    __slots__ = ('name', 'age') 

s=Student2()
s.name="jerrp"
s.age="20"
print(s.name)
print(s.age)
#限制了实例属性，导致报错
#s.classname="classname"


