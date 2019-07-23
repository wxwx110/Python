#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   23closure.py
@Time    :   2019/07/23 09:45:50
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
#定义一个函数
def test(number):

    #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d"%number_in)
        return number+number_in
    #其实这里返回的就是闭包的结果
    return test_in


#给test函数赋值，这个20就是给参数number
ret = test(20)

#注意这里的100其实给参数number_in
print(ret(100))

#注意这里的200其实给参数number_in
print(ret(200))



def counter(start=0):
    count=[start]
    def incr():
        # 引用外部函数count[]
        count[0] += 1
        return count[0]
    return incr

c1=counter(5)

print(c1())
print(c1())
# 分配了一个新的单元
c2=counter(100)
print(c2())



def counter2(start=0):
    def incr():
        # nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，
        # 如果上一级函数中不存在该局部变量，
        # nonlocal位置会发生错误
        nonlocal start
        start += 1
        return start
    return incr

c1 = counter2(5)
print(c1())
print(c1())

c2 = counter(50)
print(c2())
print(c2())


# 应用：确定了函数的最终形式(y = x + 1和y = 4x + 5)。我们只需要变换参数a,b，就可以获得不同的直线表达函数
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))
