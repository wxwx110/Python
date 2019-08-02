#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thread.py
@Time    :   2019/06/24 08:56:58
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
#current_thread永远返回当前线程的信息
#python的thread模块是比较底层的模块，python的threading模块是对thread做了一些包装的，可以更加方便的被使用
# 主线程结束，后如果子线程尚未结束，主线程会等待全部子线程完成后才结束
import time,threading
import os
def loop():
    print('thread %s is runing ... pid:%s  ppid: %s' % (threading.current_thread().name,os.getpid() ,os.getppid()))
    n=0
    while n<5:
        n=n+1
        print('thread   __%s __ %s' %(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

#如果不给子线程命名，系统会自动分配
t=threading.Thread(target=loop,name='loopThread')
t.start()
t.join()
print('thread %s ended  pid: %s ppid:%s' %(threading.current_thread().name,os.getpid(),os.getppid()))
