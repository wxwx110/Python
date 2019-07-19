#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thechardet.py
@Time    :   2019/06/26 21:30:28
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
#用于判断字符串编码
import chardet
print (chardet.detect(b'helloworld'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))