#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04filter.py
@Time    :   2019/06/15 15:37:36
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib

lisdata=range(0,10)
#filter可以根据筛选函数法，返回符合条件的序列
print(list(filter(lambda x:x%2==0,lisdata)))