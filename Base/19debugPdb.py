#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   19debug.py
@Time    :   2019/06/21 08:57:59
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

#$ python -m pdb filename.py可以单步执行
#p 变量名来查看变量
#l来查看代码
#n可以单步执行代码
#q退出

def foo(s):
    n = int(s)
    #assert的意思是，表达式n != 0应该是Truepu
    #如果断言失败，assert语句本身就会抛出AssertionError
    #python -O filefullname.py 可以关闭断言
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
main()


# import pdb
# s = '0'
# n = int(s)
# #pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：
# pdb.set_trace() 
# print(10 / n)




