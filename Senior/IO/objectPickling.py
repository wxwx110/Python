#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   objectPickling.py
@Time    :   2019/06/23 09:56:25
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import pickle

d=dict(name="baby",age="8")
print(d)
#pickling
print(pickle.dumps(d))

a=b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x04\x00\x00\x00babyq\x02X\x03\x00\x00\x00ageq\x03X\x01\x00\x00\x008q\x04u'

print(a.decode('utf-8',errors="ignore"))

# pickling and write
with open("aabbcc.text",'wb') as f:
    pickle.dump(d,f)

#read and unpickling
with open("aabbcc.text","rb") as f:
    w=pickle.load(f)
print(w)
#只代表内容相同，d,w是两个对象
print(d.__eq__(w))




