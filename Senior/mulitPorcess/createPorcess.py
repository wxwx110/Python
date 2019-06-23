#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mulitPorcess.py
@Time    :   2019/06/23 15:29:04
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
from multiprocessing import Process
from multiprocessing import Pool
import os,time,random

#Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
# 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程）
# ，然后，分别在父进程和子进程内返回。

#子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程
# ，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
#Linux nunix 可以使用fork创建进程
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

#windows Process
def run_proc(name):
    print('run Child process %s (%s)...' %(name,os.getpid()))

if __name__=="__main__":
    print('parent process %s' % os.getpid())
    #创建子进程，
    p=Process(target=run_proc,args=('test',))
    print('Child process will start')
    #开始执行子进程
    p.start()
    #等待子进程执行完成后再执行
    p.join()
    print('child process end.')


