#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03_async_yied2.py
@Time    :   2019/07/04 15:35:24
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

import time
import threading

gen=None

def long_io():
    def fun():
        #声明gen是全局变量
        global gen
        print ('开始执行耗时操作')
        # 睡眠5秒
        time.sleep(5)
        print ('完成执行耗时操作')
        result='io result'
        # 执行完成后，通过send函数返回给生成器对象gen并唤醒 yeid语句的后续其他语句执行
        try:
            gen.send(result)
        except:
            pass
    threading.Thread(target=fun,name="myfun").start()

def gen_couroutine(f):
    def wrapper():
        global gen  
        gen=f()   
        gen.send(None)
    return wrapper
    
@gen_couroutine
def req_a():
    print ('开始处理请求a')   
    ret=yield long_io()
    print(ret)
    print ('完成处理请求a')

def req_b():
    print ('开始处理请求b')
    time.sleep(2)
    print ('完成处理请求b')

def main():
    req_a()
    req_b()
    print ('end main')

if __name__ == "__main__":
    main() 