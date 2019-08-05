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

import time,threading

g_num=100000
g_flag=False
def work1():
    global g_num
    global g_flag
    for i in range(100000):
        g_num+=1
    g_flag=True
    print("g_num after work1:",g_num)
  

def work2():
    global g_num
    global g_flag
    #使用轮询的方式保证线程的执行逻辑
    #这种方式开销太大
    while True:
        if g_flag:        
            for i in range(100000):
                g_num+=1
            print("g_num after work2:",g_num)
            break
        


if __name__ == "__main__":
    t1=threading.Thread(target=work1)

    t2=threading.Thread(target=work2)

    t1.start()
    t2.start()
    


    
