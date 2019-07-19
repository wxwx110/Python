#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   15classKeyfuc.py
@Time    :   2019/06/20 15:51:37
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib

class Student(object):

    # 限定类的属性
    __slots__ = ('name', 'age') 
    # __len__让len函数可以作用一个类
    def __len__(self):
        return 5
    # toString()
    def __str__(self):
        return 'name:'+self.name +'age:'+str(self.age)
    #让调试人员能看到toString()
    __repr__=__str__
    #调用类未定义的属性时指定返回值,也可以返回一个函数
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        # 如果没有找到对应属性时的反馈
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        
a=Student()
print(len(a))
a.name="tom"
a.age=18
print(a)
print('score:',a.score)

#斐波那契数列
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    #一个类可以用于循环
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a> 10:
            # 抛出异常终止循环
            raise StopIteration()
        return self.a

    # 实现list那样按照下标取出元素
    def __getitem__(self,n):
        if isinstance(n ,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        # 实现切片
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    
for n in Fib():
    print(n)
f=Fib()

print(f[1])
print(f[1:3])


class Student2(object):
   
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        # 如果没有找到对应属性时的反馈
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#应用创建链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__

#这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
'''
有些REST API会把参数放到URL中，比如GitHub的API：

GET /users/:user/repos
调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：

Chain().users('michael').repos
'''
print(Chain().status.user.timeline.list)
#打印/status/user/timeline/list

class Student3(object):
    #可以通过实例本调用方法，无需通过方法名
    def __call__(self):
        print('call func method')
s=Student3()
s()
#callable()函数，我们就可以判断一个对象是否是“可调用”对象。
#添加了__call__函数后可以让对象成为可调用对象
print(callable(Student()))
print(callable(int))
print(callable(Student3()))
