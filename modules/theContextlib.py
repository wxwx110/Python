#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theContextlib.py
@Time    :   2019/06/25 21:42:37
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib

class Query(object):

    def __init__(self,name):
        self.name=name
    
    #使用with语法必须定义__enter__函数
    def __enter__(self):
        print('begin')
        return self

    #  #使用with语法必须定义__exit__函数
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    
    def query(self):
        print('Query info about %s' % self.name)


with Query('taobao') as f:
    f.query()

#Python的标准库contextlib提供了更简单的写法
from contextlib import contextmanager

class Query2(object):

    def __init__(self,name):
        self.name=name   

    def query(self):
        print('Query info about %s',self.name)

@contextmanager
def create_query(name):
    print('begin')
    q=Query2(name)
    yield q
    print('end')
#contextmanager这个decorator接受一个generator，
# 用yield语句把with ... as var把变量输出出去
with create_query('baidu') as q:
    q.query()



@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
# 1、with语句首先执行yield之前的语句，因此打印出<h1>；
# 2、yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 3、最后执行yield之后的语句，打印出</h1>。
with tag("h1"):
    print("hello")
    print("world")


#使用closing()把对象变为上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

#closing也是一个经过@contextmanager装饰的generator
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


