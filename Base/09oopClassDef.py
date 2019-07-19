#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09oopBase.py
@Time    :   2019/06/18 09:20:51
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
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
    #返回对象得str形式类似toString()
    def __str__(self):
        return self.name+'-'+str(self.__age)

#再类被销毁时默认会调用del方法
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.name)

a=Student("tom",20)


# print(a.getName())
# print(b.getAge())

# print(a.name)
# # age增加下划线不能直接访问
# #print(a.__age)
# # python编译器修改了改属性的名称 _类名+属性名，不同版本的解释器，可能会不同
# print(a._Student__age)

c=a
print ('1',a)

# 此时只是删除了tom对象的引用计数器
del a

print('此时tom对象还存在',2,c)
# 当有1个变量保存了对象的引用时，此对象的引用计数就会加1
# 当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，
# 那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

#此时才调用__del__方法
del c


b=Student("jerry",20)
print (3,b)
del b

