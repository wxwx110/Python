#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   16enum.py
@Time    :   2019/06/20 20:45:10
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# 枚举类，默认值从1开始
from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month)
print(Month.Jan)
for x in Month:
    print (x,x.value)

#自定义枚举值
from enum import Enum, unique

#unique 检查是否重复
@unique
class Weekday(Enum):
    Sun = 100 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for x in Weekday:
    print (x,x.value)
a=Weekday.Sun
print(a)
print(a.value)


