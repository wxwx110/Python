#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   18exception.py
@Time    :   2019/06/21 08:55:14
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
#Python内置logging 可以记录异常错误
#logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
# 指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了
import logging
#logging.basicConfig(level=logging.INFO)

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:        
        logging.exception(e)

main()
print('END')


s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)