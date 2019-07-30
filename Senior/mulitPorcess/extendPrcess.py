#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   extendPrcess.py
@Time    :   2019/07/26 10:48:58
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

from multiprocessing import Process
import time

class MyPorcess(Process):
    # 必须实现run方法
    #调用p.start()时候，默认调用run方法 
    def run(self):
        while True:
            print("---1---")
            time.sleep(1)


if __name__ == "__main__":
    
    p=MyPorcess()
    p.start()
    while True:
        print("---main---")
        time.sleep(1)
