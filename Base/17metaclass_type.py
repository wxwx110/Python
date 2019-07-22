#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   17metaclasspre.py
@Time    :   2019/07/22 08:50:09
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
# 类也是一个对象,在内存中加载
class A(object):
    pass
print (A)
print (id(A))
print(hasattr(A,'show'))
# 给类增加属性
A.show=100
print(hasattr(A,'show'))
print (A.show)
# 可以把类赋值给一个变量,并创建对象
classA=A
print(classA)
print(classA())

# 动态创建类
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo # 返回的是类，不是类的实例
    else:
        class Bar(object):
            pass
        return Bar

a=choose_class('foo')
print(a())

# 使用type创建类对象
#type(类名, 由⽗类名称组成的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

test=type('Test',(),{'a':100})
print(type(test))
print (test)
print (test().a)
## 动态创建类名字可以相同，但实际是两个不同的类
# help(test)
# test2=type('Test',(),{})
# print(type(test2))
# print (test2)
# print (test2().a)
# 动态创建A类的子类 
# test3=type('Test',(A,),{})
# print(test3)





