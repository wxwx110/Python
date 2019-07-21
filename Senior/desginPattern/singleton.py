#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   singleton.py
@Time    :   2019/07/21 15:15:58
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib


class Singleton(object):
    __instance=None
    def __new__(cls):
        if cls.__instance:
            cls.__instance=object.__new(cls)
        return cls.__instance

    def __init__(self):
        print('init called')

a=Singleton()
b=Singleton()
print(id(a),id(b),a==b)

