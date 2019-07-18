#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02collection_tuple.py
@Time    :   2019/07/18 21:17:12
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
'''
元组在字典中不可修改 但是元组中元素指向的值是可以修改的
也就是说元组中不能修改的，是元组对象存储的值或者，引用的地址（指针）

'''
b=['a','b']
a=(1,1,2,2,b)
print (a.count(1))

print(a)
#修改了元组对象list的值，元组的内容也发生了改变
# 但是并没有修改b元素指向的地址
b.append(3)
print(a)