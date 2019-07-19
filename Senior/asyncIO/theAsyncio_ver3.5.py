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

import asyncio

'''
@asyncio.coroutine
def hello():
    print('Hello World')
    #相当于base示例中的c.send(n)去执行IO操作调用其他函数
    #等待返回后，继续执行本函数的操作
    r=yield from asyncio.sleep(1)`
    print(r)
    print('hello again!')
'''
async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
print('show me the money')
loop.close()


