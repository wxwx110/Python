#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theItertools.py
@Time    :   2019/06/25 11:11:25
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import itertools

#1 顺序迭代器
naturals=itertools.count(1)
for x in naturals:
    print(x)
    if x==10:
        break

#itertools.count(1) 一但创建调用一次后，不会从头重新计数
#如果不加这一句，下面的截取返回空list
naturals=itertools.count(1)
#截取序列的一部分
ns=itertools.takewhile(lambda x:x<=10 ,naturals)
print (list(ns))


#2 无限循环迭代器，无限重复abc
# cs=itertools.cycle('abc')
# for x in cs:
#     print(x)

# 3 单个元素循环迭代器，第二个参数表示循环次数，默认可以为空
ns=itertools.repeat('a',3)
for x in ns:
    print(x)


#串联迭代对象
for x in itertools.chain('zzz','bbb'):
    print(x)

#对象分组
#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key,group in itertools.groupby('AaaBbbEccdDd'):
    print (key,list(group))
print('________________________________')
#
#挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的  
#通过自定义挑选函数忽略大小写
for key,group in itertools.groupby('AaaBbbEccdDd', lambda c: c.upper()):
    print (key,list(group))


