#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14oopClassMethod.py
@Time    :   2019/07/20 10:24:42
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

class Car(object):

    carType='奥迪'
   

    def __init__(self, *args, **kwargs):       
        self.carType='奔驰'

    # 类方法可以通过实例引用，也可以通过类名引用
    #类方法传入的参数是 类本身，而不是对象访问的是类属性
    @classmethod
    def getCarType(clss):
        print(type(clss))
        print(isinstance(clss,Car))
        return 'clsssmethod'+ clss.carType

    def getCarType2(self):
        print(type(self))
        print(isinstance(self,Car))
        return self.carType


    #静态方法，不需要定义参数直接使用类名调用类属性
    @staticmethod   
    def getCarType3():
        return Car.carType

car=Car()

print ('car.getCarType()-----',car.getCarType())
print ('Car.getCarType()-----',Car.getCarType())

print ('car.getCarType2()-----',car.getCarType2())

print ('Car.getCarType3()-----',car.getCarType3())
print ('Car.getCarType3()-----',Car.getCarType3())

