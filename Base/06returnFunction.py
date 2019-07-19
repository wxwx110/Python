#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   06returnFunction.py
@Time    :   2019/06/16 10:11:11
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib

# 将函数作为方法的返回值
def lazy_sum(*args):
    def sum():
        res=0
        for x in args:
            res=res + x
        return res
    return sum
intList=[1,2,3,4,5]

func=lazy_sum(*intList)
func2=lazy_sum(*intList)
# 得到的是函数
print('得到的是函数',func)
#得到的是函数计算结果
print('得到的是计算结果',func())

#每次调用生成的都是新的对象
print(func==func2)
# 闭包，函数f()引用了循环变量i
# 返回的函数在其定义内部引用了局部变量i，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
# i并不会被重新声明，而是一直保持
# 因此返回函数不要引用任何循环变量，或者后续会发生变化的变量
# def count():
#     fs=[]
#     for i in range(1,4):
#         print("循环开始 ",i)
#         def f():
#             print ("调用返回值函数此时的I=",i)
#             return i*i
#         fs.append(f)
#     return fs
# # 给变量赋值，此时已经完成for循环 i=3
# f1,f2,f3=count()

# print("准备调用函数返回结果")
# # 调用返回结果时 i永远等于3
# print(f1())
# print(f2())
# print(f3())

#处理闭包引用可变量的方法
def count2():
    def f(x):              
        def b():
            print ("用返回值函数此时的I=",x)  
            return x*x
        return b
    
    fs=[]
    # 调用时，才开始进行循环，函数返回的是一个列表创建了三个func
    for i in range(1,4):        
        print("循环开始 此时的i",i)
        fs.append(f(i))
    # print(list(fs))
    print("fs.count",len(fs))
    return fs


f1,f2,f3=count2()

print("准备调用函数返回结果")
print(f1())
print(f2())
print(f3())

# 返回一个方法列表，包含三个function
# f4=count2()
# print(f4)
