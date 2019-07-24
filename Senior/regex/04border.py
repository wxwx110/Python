#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04border.py
@Time    :   2019/07/24 22:14:59
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

'''
^	匹配字符串开头
$	匹配字符串结尾
\b	匹配一个单词的边界
\B	匹配非单词边界

'''
import re

# 正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.com")
print(ret.group())

# 不正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei")
print(ret.group())

# 通过$来确定末尾
# ret = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.comheihei")
# print(ret.group())


print(re.match(r".*\bver\b", "ho ver abc").group())

# 不能匹配
# print(re.match(r".*\bver\b", "ho verabc").group())

#print(re.match(r".*\bver\b", "hover abc").group())


print(re.match(r".*\Bver\B", "hoverabc").group())

# 不能匹配
# print(re.match(r".*\Bver\B", "ho verabc").group())
