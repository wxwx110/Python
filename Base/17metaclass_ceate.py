#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   17metaclass_ceate.py
@Time    :   2019/07/22 11:06:46
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
# 定义元类让类的属性都大写
def upper_attr(future_class_name, future_class_parents, future_class_attr):

    print('future_class_name:',future_class_name)
    print('future_class_parents:',future_class_parents)
    print('future_class_attr:',future_class_attr)
    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)

'''
元类的核心作用
1拦截类的创建
2、修改类
3、返回修改之后的类
'''
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情

    def __new__(cls, future_class_name, future_class_parents, future_class_attr):
        #遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name,value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, newAttr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, newAttr)

        # 方法3：使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, newAttr)




class Foo(object, metaclass = UpperAttrMetaClass):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出:True

f = Foo()
print(f.BAR)
# 输出:'bip'