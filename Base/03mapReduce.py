#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03mapReduce.py
@Time    :   2019/06/15 09:48:03
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
from functools import reduce


# dataList=[1,2,3,4,5]

# def doubleNum(x):
#     return x*x

# # map接收参数
# # 第一个参数表示传入的方法
# # 第二个参数，接收一个Iterable 可以是list tuple 或者字符串等
# #返回对象位一个Iterator
# print(list(map(doubleNum,dataList)))
# print("返回的是一个Iterator对象:",map(doubleNum,dataList))


# def sum(x,y):
#     # x接收的是上一次SUM函数运行的结果
#     print('x:',x)
#     # y参数是Iterable的next值
#     print('y:',y)
#     return x+y

# # reduce 可以把上一次函数运算的结果作为参数传入下一次运算中进行运算
# print(reduce(sum,dataList))


# #组合函数将字符串转换成对应的INT值
# digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def fn(x,y):
#         return x*10+y
# def getChar(x):
#     return digits[x]
    
# def getStringToInt(strings):
#     return reduce(fn,map(getChar,strings))

# print(getStringToInt("9527"))

# # 函数整理
# def getStringToInt2(strings):
#     def fn(x,y):
#         return x*10+y
#     def getChar(x):
#         return digits[x]
#     return reduce(fn,map(getChar,strings))

# print(getStringToInt2("9527"))

# # lamda简化
# def getStringToInt3(s):
#     return reduce(lambda x, y: x * 10 + y, map(getChar, s))

# print(getStringToInt3("9527"))


# def getStringToInt4(s):
#     return reduce(lambda x, y: x * 10 + y, map(lambda x:digits[x],s))

# print(getStringToInt4("9527"))


# nameList=['adam', 'LISA', 'barT']
# def change(x):
    
#     return x[0].upper() +x[1:].lower()



# # 输入名字，让首字母大写cl
# def changeName(nameInput):
#     return map(change,nameList )
# print(list(changeName(nameList)))

# #编写函数求列表乘积
# listData=[3,5,7,9]
# def prod(list):
#     return reduce(lambda x,y : x*y,listData)
# print(prod(listData))

#把字符串转换成浮点数
def changeChar(x,y):  
    if isinstance(y,(int)):
        return x*10+y
    else:
        return x+y

def change2Float(s):
    return reduce(changeChar,map(lambda x:x,s))


print(change2Float("3.1415"))




   



