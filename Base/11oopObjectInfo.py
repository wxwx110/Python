#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11oopObjectInfo.py
@Time    :   2019/06/18 15:32:26
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
print("_______________type_____________")
# type()返回对象对应的class类型
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
class A:
    pass
a=A()
print(type(a))

print(type(123)==type(456))

print(type(123)==int)

print(type('abc')==type('123'))

print(type('abc')==str)

print(type('abc')==type(123))

#types模块中定义的常量 可以判断函数类型
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print("_______________instance_____________")
#isinstance()判断继承关系
class Animal(object):
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class MiniDog(Dog):
    pass
dog=Dog()
miniDog=MiniDog()

print(isinstance(dog,Animal))
print(isinstance(miniDog,Animal))


print("_______________dir_____________")

#__XXX__的特殊用法
#在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，
# 在len()函数内部，它自动去调用该对象的__len__()方法
class MyDog(object):
    def __init__(self):
        self.x=9
    
    def __len__(self):
        return 100

    def getDouble(self):
        return self.x*self.x
    def getX(self):
        print (self.x)

dog = MyDog()
print(len(dog))
#dir获取对象的全部属性和方法
print(dir("123"))
mydog=MyDog()

#判断是否有某个属性
print(hasattr(mydog, 'x'))

#获取属性值，同样也可活的方法
print(getattr(mydog,'x'))

print(setattr(mydog, 'x', 10))
mydog.getX()
print(getattr(mydog,'x'))





