#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02List.py
@Time    :   2019/06/14 16:35:44
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# list 可变长的列表,可混合元素
a=[1,2,3,4,5,6,7,8,9,10,'a']
print(a)
# 添加元素
a.append(11)
# 弹出元素并返回改元素
print(a.pop())
a.insert(1,'b')
print(a)
def func(b):
    b.append(12)
    print(b)
func(a)
print(a)
print("从索引1开始取到索引2不包含索引2",a[1:2])
print("取前两个元素",a[:2])
print("取后两个元素",a[-2:])
print("复制组",a[:])





