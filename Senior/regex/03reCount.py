#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03reCount.py
@Time    :   2019/07/24 11:17:13
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
'''
*	匹配前一个字符出现0次或者无限次，即可有可无
+	匹配前一个字符出现1次或者无限次，即至少有1次
?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	匹配前一个字符出现m次
{m,}	匹配前一个字符至少出现m次
{m,n}	匹配前一个字符出现从m到n次
'''
import re

# 0次无限次
ret=re.match('[a-z][A-Z]*','a')
print(ret.group())
ret=re.match('[a-z][A-Z]*','aBC')
print(ret.group())

# 1次无限次
ret=re.match('[a-z][A-Z]+','aB')
print(ret.group())
ret=re.match('[a-z][A-Z]+','aBC')
print(ret.group())

# 1次或者0次
ret=re.match('[a-z][A-Z]?','aB')
print(ret.group())
ret=re.match('[a-z][A-Z]?','aBC')
print(ret.group())

#出现n次
ret=re.match('[a-z][A-Z]{1}','aB')
print(ret.group())
ret=re.match('[a-z][A-Z]{2}','aBC')
print(ret.group())

#出现m次到n次
ret=re.match('[a-z][A-Z]{1,2}','aBC')
print(ret.group())