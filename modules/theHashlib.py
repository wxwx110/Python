#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theHashlib.py
@Time    :   2019/06/25 09:46:51
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import hashlib

#1 md5
md5=hashlib.md5()
md5.update('show me the money'.encode('utf-8'))
print(md5.hexdigest())

# 可以分批次
md6=hashlib.md5()
md6.update('show me '.encode('utf-8'))
md6.update('the money'.encode('utf-8'))
print(md6.hexdigest())

# 2 hmac算法
import hmac
message=b'show me the mony'
key=b'showme'
h=hmac.new(key,message,digestmod='MD5')
# 如果消息很长可以多次调用update
print(h.hexdigest())