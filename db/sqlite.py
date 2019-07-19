#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sqlit.py
@Time    :   2019/06/27 10:30:47
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
#SQLite的驱动内置在Python标准库中
import sqlite3
#果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')

# 创建一个Cursor:
cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)
# cursor.close()
# #提交事务
# conn.commit()

# conn.close()

conn=sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
cursor.execute('select * from user where id=?', ('1',) )
values=cursor.fetchall()
print(values)
cursor.count()
conn.close()


