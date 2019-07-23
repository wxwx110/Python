#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   22iterator.py
@Time    :   2019/07/23 08:56:35
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
'''
一类是集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等；

一类是 generator ，包括生成器和带 yield 的generator function。

这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable 。
'''
from collections.abc import Iterable,Iterator

print(isinstance([],Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# iterable 不等于iterator
# 可以使用iter()函数变成iterator

print(isinstance([],Iterator))
print(isinstance(iter([]),Iterator))