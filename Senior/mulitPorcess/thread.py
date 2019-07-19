#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thread.py
@Time    :   2019/06/24 08:56:58
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
#current_thread永远返回当前线程的信息
import time,threading

def loop():
    print('thread %s is runing ...' % (threading.current_thread().name))
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
print('thread %s ended' %threading.current_thread().name)
