#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07decorator.py
@Time    :   2019/06/17 10:11:12
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
def now():
    print("2015-03-25")

f=now
f()

# 函数对象的属性
print(now.__name__)

# 增强now函数功能，但不修改now代码使用装饰器
# 本质上，decorator就是一个返回函数的高阶函数
# 装饰器函数在调用装饰函数前进行调用，听过装饰器定义的操作可以定义
# 被装饰函数的执行
def log(func):
    def wrapper(*args,**kw):
        print("调用装饰器定义函数")
        print(list(*args))
        print(dict(**kw))
        print(args[0])
        if  args[0]=='tudou':
            print('call %s()：' %func.__name__)
            return func(*args,**kw)
        else:
            print("not call %s()：" %func.__name__)
    return wrapper

# 把@log放到now()函数的定义处，相当于执行了语句
# now = log(now)
#于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
@log
def now2(name,**kw):
    print("调用函数体")
    print("hello:",name)
now2("tudou",key="123" ,value="456")
now2("2udou",key="123" ,value="456")

print("now2.name:",now2.__name__)


print('---------接收参数的decorator------------')
#接收参数的decorator
# 3层嵌套的效果是这样的 now = log('execute')(now)
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数
# 但是此时由于(now)执行后得到的是wrapper函数一次now函数的__name__属性会变成wapper
#通过  @functools.wraps(func)可以避免这个问题
import functools

def log2(text):
    def mydecorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):      
            print("geParameter %s" % text)      
            if args[0]=="tudou":
                return func(*args,**kw)
            else:                
                print("func:%s is not call " % func.__name__)
        return wrapper
    return mydecorator


@log2("showme")
def now3(name,**kw):
    print("调用函数体")
    print("hello:",name)
now3("tudou",key="123" ,value="456")
now3("2udou",key="123" ,value="456")
print("now3.name:",now3.__name__)

    



