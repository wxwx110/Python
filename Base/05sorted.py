#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   05sorted.py
@Time    :   2019/06/15 15:43:29
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

intList=[6,7,8,2,2,7,8,0,-3,42,]
# 升序排序
print(sorted(intList))
#降序排序
print(sorted(intList,reverse=True))
# 绝对值排序
print(sorted(intList,key=abs))

stringlist=['bob', 'about', 'Zoo', 'Credit']
# ascii排序
print(sorted(stringlist))
#按字母升序排序
print(sorted(stringlist,key=str.lower))
#按字母升倒叙排序
print(sorted(stringlist,key=str.lower,reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#自定义规则排序
def sortByName(t):
    return t[0]
print (sorted(L,key=sortByName,reverse=True))


def sortByScore(t):
    return t[1]
print (sorted(L,key=sortByScore))

