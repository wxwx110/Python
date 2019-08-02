#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pool.py
@Time    :   2019/06/23 16:18:28
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''
from multiprocessing import Pool
import os,time,random
# here put the import lib
#Process pool
'''
apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；

apply(func[, args[, kwds]])：使用阻塞方式调用func

close()：关闭Pool，使其不再接受新的任务；

terminate()：不管任务是否完成，立即终止；

join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；

'''
def long_time_task(name):
    print('Ran task %s (%s)... fatherId:%d' %(name,os.getpid(),os.getppid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task%s runs %0.2f seconds.' %(name,(end-start)))
#调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process
if __name__=='__main__':
    print('Parent process %s' %os.getpid())
    #限制只有4个进程同时执行，默认与CPU核心数相同
    p=Pool(4)
    for i in range(6):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    # 关闭进程池不再接收新的任务
    p.close()
    # 等待所有进程完成，必须放在close后
    p.join()
    print('Allsubprocesses down.')