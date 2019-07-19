#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   JSON.PY
@Time    :   2019/06/23 10:38:22
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import json
#dic to JSON
d=dict(name="taobao",age="8")
print(json.dumps(d))

#json to dic
e=json.loads('{"name": "taobao", "age": "8"}')
print(type(e))
print(e)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# 对象不能直接JSON化，需要通过实转换函数
#先转换成dict在JSON化
#print(json.dumps(s))
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s,default=student2dict))

#lambda obj: obj.__dict__可以把任意对象先变成dict但是定义了__slots__的class除外
print(json.dumps(s, default=lambda obj: obj.__dict__))

#对象反序列化必须先定义函数从dic到对象
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads('{"name": "Bob", "age": 20, "score": 88}',object_hook=dict2student))

