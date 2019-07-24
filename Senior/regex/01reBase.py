#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01reBase.py
@Time    :   2019/07/24 10:10:03
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import re

result=re.match('it','itit it 3')

print(result.group())

ret = re.search(r"\d+", "阅读次数为 9999 2222")
print(ret.group())

# 返回匹配的元素集合
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print ('re.findall',ret)

# 将匹配的数据进行替换
ret = re.sub(r"\d+", '998', "python = 997")
print (ret)