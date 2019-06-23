#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   processConmunicate.py
@Time    :   2019/06/23 16:28:26
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write :%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read : %s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue,' % value)

#在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用
# ，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
if __name__=='__main__':
    #父进程创建Queue ,并传递给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动写进程
    pw.start()
    # 启动读进程
    pr.start()
    #等待写进程结束
    pw.join()
    # PR进程无限循环，强行终止
    pr.terminate()


