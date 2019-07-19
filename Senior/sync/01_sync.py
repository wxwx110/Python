#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_sync.py
@Time    :   2019/07/04 10:00:28
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import time

def long_io():
    print ('开始执行耗时操作')
    # 睡眠5秒
    time.sleep(5)
    print ('完成执行耗时操作')
    result='io result'
    return result

def req_a():
    print ('开始处理请求a')
    ret=long_io()
    print (ret)
    print ('完成处理请求a')

def req_b():
    print ('开始处理请求b')
    print ('完成处理请求b')

def main():
    req_a()
    req_b()
    

if __name__ == "__main__":
    # 同步，程序会按照顺序进行执行遇到阻塞（IO），等待阻塞完成后才继续执行
    main()