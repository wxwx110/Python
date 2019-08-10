#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   threadlocalvar.py
@Time    :   2019/06/24 11:46:43
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import threading,time


# 线程的非全局变量，线程空间是各自独立独有的


def work1():
    g_num=100
    g_num+=1
    print("g_num after work1:",1,g_num)
    time.sleep(2)
    print("g_num after work1:",2,g_num)

def work2():
    time.sleep(1)
    g_num=1
    print("g_num after work2:",1,g_num)
    
        


if __name__ == "__main__":
    t1=threading.Thread(target=work1,)

    t2=threading.Thread(target=work2)

    t1.start()
    t2.start()
