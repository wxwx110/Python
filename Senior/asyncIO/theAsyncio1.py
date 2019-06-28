#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theAsyncio.py
@Time    :   2019/06/28 14:47:44
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

import asyncio

@asyncio.coroutine
def hello():
    print('Hello World')
    #相当于base示例中的c.send(n)去执行IO操作调用其他函数
    #等待返回后，继续执行本函数的操作
    r=yield from asyncio.sleep(1)
    print(r)
    print('hello again!')

loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
print('show me the money')
loop.close()
'''
@asyncio.coroutine把一个generator标记为coroutine类型，然后就把这个coroutine扔到EventLoop中执行。

hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，
而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，
线程就可以从yield from拿到返回值（此处是None），
然后接着执行下一行语句。

把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，
而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
'''

