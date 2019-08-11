#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   async_base.py
@Time    :   2019/08/10 10:35:46
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"

def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

def main():
    pool = Pool(3)
    pool.apply_async(func=test,callback=test2)

    # time.sleep(5)
    pool.close()

    pool.join()

    print("----主进程-pid=%d----"%os.getpid())

if __name__ == "__main__":
    main()
