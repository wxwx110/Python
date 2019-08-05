#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   threadglobalvar_poll.py
@Time    :   2019/08/03 23:03:07
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
# 使用锁的方式，占用资源更小
import time,threading

g_num=100000

# 创建互斥锁
mutex=threading.Lock()

def work1():
    global g_num
    # 上锁
  
    for i in range(100000):
        mutex.acquire()
        g_num+=1
    # 解锁
        mutex.release()
    print("g_num after work1:",g_num)
  

def work2():
    global g_num
      # 上锁
    
    for i in range(100000):
        mutex.acquire()
        g_num+=1
    # 解锁
        mutex.release()
    print("g_num after work2:",g_num)
    
        


if __name__ == "__main__":
    t1=threading.Thread(target=work1,)

    t2=threading.Thread(target=work2)

    t1.start()
    t2.start()
    


    
