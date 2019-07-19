#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stringIOAndBytesIO.py
@Time    :   2019/06/21 16:54:40
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
from io import StringIO

f=StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print (f.getvalue())



f = StringIO(r'Hello!\nHi!\nGoodbye!')
for x in f.readlines():
    print(x.strip())

from io import BytesIO
f=BytesIO()
f.write('天下'.encode('UTF-8'))
print(f.getvalue())
print('WRITE',f.getvalue().decode("UTF-8"))

f=BytesIO(b'\xe5\xa4\xa9\xe4\xb8\x8b')
print('READ',f.read().decode("UTF-8"))