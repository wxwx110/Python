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
import time,os
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
        except StopIteration:
            pass
    threading.Thread(target=fun).start()

# 通过yield取消了回调函数，将调用和打印集中到req_a()函数
def req_a():
    print ('开始处理请求a',threading.current_thread().name,os.getpid())    
    ret=yield long_io()   
   # 因为使用了多线程前后 yeid返回后其实是在线程中执行的
    print ('完成处理请求a' ,threading.current_thread().name,os.getpid())

    print(ret)

def req_b():
    print ('开始处理请求b')
    time.sleep(2)
    print ('完成处理请求b')

def main():
    global gen
    # req_a通过yied关键字已经变成一个生成器
    #gen=req_a()是生成 需要执行的代码req_a()定义的函数体，以及，执行该代码包含的上下文环境
    gen=req_a()
    # 调用next（）开始执行，req_a()的语句指导yield关键字，并返回yield右边的内容，
    # 如果yied 右边 定义的内容是函数/生成器，则调用该函数/生成器
    # gen.send(None) 或者next(gen)
    next(gen)

    req_b()
    print ('end main')
    

if __name__ == "__main__":
    main() 