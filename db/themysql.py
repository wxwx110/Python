#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mysql.py
@Time    :   2019/06/27 10:46:37
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import mysql.connector
conn=mysql.connector.connect(user='root', password='root', database='testPython')
cursor=conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#注意mysql的占位符
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)

conn.commit()
cursor.close()
cursor=conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()