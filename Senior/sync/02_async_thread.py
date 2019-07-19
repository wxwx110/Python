#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_sync.py
@Time    :   2019/07/04 10:00:28
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import time
import threading

def long_io(callbakc_func):
    def fun(callback):
        print ('开始执行耗时操作')
        # 睡眠5秒
        time.sleep(5)
        print ('完成执行耗时操作')
        result='io result'
        callback(result)
    threading.Thread(target=fun,args=(callbakc_func,),name="myfun").start()
   

def callBackFunc(result):
    print('开始执行回调打印')
    time.sleep(2)
    print(result)

def req_a():
    print ('开始处理请求a')
    ret=long_io(callBackFunc)
   
    print ('完成处理请求a')

def req_b():
    print ('开始处理请求b')
    print ('完成处理请求b')

def main():
    req_a()
    req_b()
    print ('end main')

if __name__ == "__main__":
    main() 