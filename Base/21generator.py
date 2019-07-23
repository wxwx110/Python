#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   21generator.py
@Time    :   2019/07/22 16:15:33
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
'''
generator 生成器，用通过表达式进行循环计算得出结果
'''
# a是一个列表 b是一个生成器，
# a在内存中已经分配了1-9的存储单元
# b在内存中只是一个表达式并没有生成数字
# 因此b比较a更能节省内存单元
a=[x for x in range(1,10)]
b=(x for x in range(1,10))
print (a)
print(b)
# 通过next获取b的值
print(next(b))

# 生成器定义
def fib(times):
    n = 0
    a,b = 0,1
    while n<times:
        # 中断并返回 b值
        yield b
        a,b = b,a+b
        n+=1
    return 'done'
# 只能获得 yield的返回值 不能获得return值
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
for x in fib(5):   
        print(x)

g=fib(5)
while True:
    try:
        x = next(g)
        print("value:%d"%x)      
    except StopIteration as e:
        print("生成器返回值:%s"%e.value)
        break
    
print('*'*10)
def createAndGet():
    print('genterator Begin')
    time=5
    for x in range(0,time):
        print('genterator for Begin')
     
        getValue=yield x
        print ('after:x:',x)
        print('getValue',getValue)
    

d=createAndGet()

'''
这段代码我自己也懵B了
'''
for n in d:
   
    d.send(n)
    print('n:',n)
