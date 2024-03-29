#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   threadglobalvar.py
@Time    :   2019/08/03 10:50:30
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import threading,time

# 当使用可变类型例如list dic等作为参数时，即使不用global也会导致公用
g_num=100

def work1():
    # 如果再线程中需要修改该值，则先用global申明，否则直接引用即可
    global g_num
    for i in range(3):
        g_num+=1
    print("g_num in work1:",g_num)

def work2():
    global g_num
    print("g_num in work2:",g_num)


t1=threading.Thread(target=work1)

t1.start()
time.sleep(1)
t2=threading.Thread(target=work2)
t2.start()

print("g_num in main Thread:",g_num)


