#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   asyncBase.py
@Time    :   2019/06/28 09:45:15
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import threading,os
def customer():
    r=''
    while True:
        # yieid 即作为generator的返回值，返回 send函数的调用结果
        # yieid 也作为 send函数的入口，接收send函数传入的参数，并执行后续的逻辑
        n=yield r
        if not n:
            return
        print('[consumer] consuming %s...' % n)
        r='200 OK'

def produce(c):
    #c.send(None)第一次调用会激活启动generator() 从r=''开始执行
    
    k=c.send(None)
    n=0
    while n<2:
        n=n+1
        print('[PRODUCER] Producing %s...' % n)
        print('before:',threading.current_thread().name,os.getpid())
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
        print('after',threading.current_thread().name,os.getpid())
    c.close()

'''
Python对协程的支持是通过generator实现的。
在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
首先调用c.send(None)启动生成器；
然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
consumer通过yield拿到消息，处理，又通过yield把结果传回
produce拿到consumer处理的结果，继续生产下一条消息；
produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
'''
c=customer()
produce(c)