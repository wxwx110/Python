#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02reChar.py
@Time    :   2019/07/24 10:43:15
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

'''
.	匹配任意1个字符（除了\n）
[ ]	匹配[ ]中列举的字符
\d	匹配数字，即0-9
\D	匹配非数字，即不是数字
\s	匹配空白，即 空格，tab键
\S	匹配非空白
\w	匹配单词字符，即a-z、A-Z、0-9、_
\W	匹配非单词字符
'''
import re
ret = re.match(".","a")
print(ret.group())


ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]","7Hello Python")
ret.group()

    # 匹配0到9第二种写法
ret = re.match("[0-9]","7Hello Python")
ret.group()

ret = re.match("嫦娥1号","嫦娥1号发射成功")
print (ret.group())
ret = re.match("嫦娥2号","嫦娥2号发射成功")
print (ret.group())
ret = re.match("嫦娥\d号","嫦娥1号发射成功")
print (ret.group())
ret = re.match("嫦娥\d号","嫦娥2号发射成功")
print (ret.group())

mm = "c:\\a\\b\\c"
ret = re.match("c:\\\\a",mm)
print(ret.group())
#python中字符串前面加上 r 表示原生字符串,没有转义字符
ret = re.match(r"c:\\a",mm)
print(ret.group())

