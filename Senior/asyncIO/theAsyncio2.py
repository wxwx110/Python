#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theAsyncio.py
@Time    :   2019/06/28 14:47:44
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

import threading
import asyncio


@asyncio.coroutine
def hello(n):
  
    
    print('%s Hello world! (%s)' % (n,threading.currentThread()))
    #1、hello(0) 执行print('%s Hello world! (%s)' 
    #2、开始执行yield from asyncio.sleep(1) 相当于调用协程执行IO操作
    #3、主程不等待，继续执行hello(1)  执行print('%s Hello world! (%s)' 
    #4、协程返回开始执行 hello(0)的 print('%s Hello again! (%s)' %
    #5、协程返回开始子执行 hello(1)的 print('%s Hello again! (%s)' %

    yield from asyncio.sleep(1)
    print('%s Hello again! (%s)' % (n,threading.currentThread()))
    
n=0
loop = asyncio.get_event_loop()
tasks = [hello(n), hello(n+1)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
