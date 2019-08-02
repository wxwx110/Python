#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   threadlock.py
@Time    :   2019/06/24 11:07:53
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

import time,threading

balance=0

#create lock
lock=threading.Lock()


def change_balance(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(1000000):
        change_balance(n)

def run_thread2(n):
    for i in range(1000000):
        #先获取锁
        lock.acquire()
        try:
            change_balance(i)
        finally:
            #释放锁
            lock.release()

print('Run thread with out lock')
t1=threading.Thread(target=run_thread,args=(2,))
t2=threading.Thread(target=run_thread,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

print('Run thread with  lock')
balance=0
t1=threading.Thread(target=run_thread2,args=(2,))
t2=threading.Thread(target=run_thread2,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#Python的线程虽然是真正的线程，但解释器执行代码时，
# 有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁
#然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
#Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
# 多个Python进程有各自独立的GIL锁，互不影响


