#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10oopExtends.py
@Time    :   2019/06/18 14:44:41
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
       print('Dog is running...')


    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()
print(isinstance(dog,(Animal)))

class Timer(object):
    def run(self):
        print('Start...')


def autoRun(animal):
    animal.run()

#autoRun方法，多态应用
autoRun(dog)
autoRun(cat)

#Python动态语言支持，非Animal得子类，只要实现了相同得方法一样可以调用
autoRun(Timer())
