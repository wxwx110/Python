#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01helloworld.py
@Time    :   2019/06/13 21:39:28
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

# 使用*c申明可变参数
def sum(a=0,b=0,*c):
    sum=0
    for x in c:
        sum+=x
    else :
        print('endofor')
    return sum+a+b

p=[1,1]
# 使用#p可以将list的每一项作为参数传入可变参数函数
print(sum(5,5,*p))


# 关键字参数，再指定参数值时，同时可以指定参数名称
def person(name,age,**other):
    print('name',name,'age',age,'other',other)

person('天使',20)

person('恶魔',20,city="地狱",shuxing="火")

t={'city':'地狱','kg':50}
person('恶魔',20,**t)

# 限定关键字参数，参数名
# 限定命名参数只能是city,kg，使用特殊分隔符 *区分
def person2(name,age,*, city,kg):
    print('name',name,'age',age,'city',city,'kg',kg)



t={'city':'地狱','kg':50}
person2('恶魔',20,**t)
t={'cc':'地狱','dd':50}
#当传入的参数名称与限定不服时，会导致错误
#person2('恶魔',20,**t)


def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

person3('杰克',4,*t,city="天下",job="医生")

# 函数的递归调用
def move(n,a,b,c):
    if n == 1:
         print(a, '-->', c)
    else:
        move(n-1,a,c,b) #把a上的n-1个盘子借助c移动到b
        move(1,a,b,c)   #把a上1个盘子移动到c
        move(n-1,b,a,c) #把b上的n-1个盘子借助a移动到c

move(3,'a','b','c')


