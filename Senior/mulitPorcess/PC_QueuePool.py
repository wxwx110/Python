#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PC_QueuePool.py
@Time    :   2019/07/30 17:15:25
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

from multiprocessing import Manager,Pool


def setter(q):
    for x in range(5):
        
        q.put(x)
        print('set %s' %x)

def getter(q):
    while True:
        if not q.empty():
            print('get %s ' %q.get(True))

if __name__ == "__main__":
    
    # 进程池中的队列需要使用Manager()来创建
    q=Manager().Queue()

    p=Pool(4)

    p.apply_async(setter,(q,))

    p.apply_async(getter,(q,))
    p.close()
    p.join()
    print("main Porcess end")