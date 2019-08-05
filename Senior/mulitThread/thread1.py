#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thread1.py
@Time    :   2019/08/03 09:24:31
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import time ,threading,os
import random

'''
系统开机会创建2个基本进程：
0号进程负责，进程的调度
1号进程，负责创建其他所有进程，并负责回收孤儿进程

僵尸进程：是当子进程比父进程先结束，而父进程又没有回收子进程，释放子进程占用的资源，此时子进程将成为一个僵尸进程。

孤儿进程：如果父进程先退出 ，子进程称为孤儿进程 被init（1号进程）接管，子进程退出后init会回收其占用的相关资源
'''
def threadTask(taskno):
    print("thread %s Begin" % taskno)
    time.sleep(random.randint(1,4))
    print("current task no %s pid: %s ppid:%s current_task_name:%s" %(taskno,os.getpid(),os.getppid(),threading.currentThread().name))


def main():
    for i in range(5):
        currentTask=threading.Thread(target=threadTask,args=(i,))
        currentTask.start()

if __name__ == "__main__":
    print("main pid %s ppid:%s"%(os.getpid(),os.getppid()))
    main()
    print("main complete")
    
