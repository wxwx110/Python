#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   processPoolApply.py
@Time    :   2019/07/30 11:20:41
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
from  multiprocessing import Pool
import time,os

def subFunc(num):
    print("sub process %s Begin pid:%d  ppid :%d" %(num,os.getpid(),os.getppid()))
    time.sleep(2)
    print("sub process %s end" %num)


if __name__ == "__main__":
    print("main porcess start pid:%d" %os.getpid())
    p=Pool(3)
    for i in range(6):
        # 堵塞式执行，子任务顺序执行不能异步
        p.apply(subFunc,(i,))
    p.close()
    p.join()
    print("process main end")