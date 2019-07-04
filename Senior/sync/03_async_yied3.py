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
   
    print ('开始执行耗时操作')
    # 睡眠5秒
    time.sleep(5)
    print ('完成执行耗时操作')
    result='io result'
    print(5,'准备返回loop_io执行结果')
    yield result
     
def gen_couroutine(f):
    def wrapper():
        print(1,'进入装饰器执行')
        global gen  
        gen=f() 
        # 调用req_a()构造器通过语句 yied long_io()  得到  long_io()构造器        
        gen_long_io=gen.send(None)
        def fun():
            print (4,'开始执行long_io构造器')
            ret = gen_long_io.send(None)
            print(6,'返回loop_io执行结果')
            try: 
                print(7,'将long_io的执行结果返回req_a()构造器')
                gen.send(ret)
            except StopIteration:
                pass
        # tournado的异步是用epoll交互替代了thread部分
        #开始执行线程，调用fun(函数)
        print(3,'调用多线程')
        threading.Thread(target=fun,name="myfun").start()
    return wrapper
    
@gen_couroutine
def req_a():
    print(2,'开始执req_a()构造器，通过yeid 返回 long_io构造器')
    print ('开始处理请求a')   
    ret=yield long_io()
    print (8,'打印long_io()的执行结果')
    print(ret)
    print ('完成处理请求a')

def req_b():
    print ('异步IO开始处理请求b')
    time.sleep(2)
    print ('完成处理请求b')

def main():
    req_a()
    req_b()
    print ('end main')

if __name__ == "__main__":
    main() 