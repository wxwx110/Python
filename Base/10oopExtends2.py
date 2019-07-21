#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10oopExtends2.py
@Time    :   2019/07/20 09:14:17
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

#coding=utf-8
class base(object):
    def test(self):
        print('----base test----')


class A(base):
    def test(self):
        print('----A test----')

        # 定义一个父类
class B(base):
    def test(self):
        print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass

class D(B,A):
    pass


obj_C = C()
obj_C.test()
#可以查看C类的对象搜索方法时的先后顺序
#如果基类具有相同的方法名时，
# 调用顺序是
# 1、类定义时继承基类的顺序
# 2、继承类的基类
print(C.__mro__) 


obj_D=D()

print(D.__mro__)