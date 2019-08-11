#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2019/08/10 16:03:36
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
from ctypes import *
from threading import Thread

# 加载动态库
lib=cdll.LoadLibrary("./libdeadloop.so")

# 创建一个子进程,让其执行C语言白那些的函数，此函数是一个死循环

t=Thread(target=lib.DeadLoop)
t.start()

#主线程，也调用C语言编写的死循环函数
lib.DeadLoop()


while True:
    pass
