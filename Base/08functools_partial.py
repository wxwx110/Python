#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   08functools_partial.py
@Time    :   2019/06/17 16:52:18
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import functools
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
#如果传入base参数，就可以做N进制的转换
print(int('12345',base=7))
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=7 )
print(int2('12345'))