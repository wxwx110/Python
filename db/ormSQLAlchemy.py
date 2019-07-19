#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ormSQLAlchemy.py
@Time    :   2019/06/27 14:31:54
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基础类
Base=declarative_base()

# 定义User对象
class User(Base):
    # 数据库表名
    __tablename__='user'

    id=Column(String(20),primary_key=True)
    name=Column(String(20))

# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine=create_engine('mysql+mysqlconnector://root:root@localhost:3306/testPython')

# 创建DBSession类型
DBSession=sessionmaker(bind=engine)

# 添加
# session=DBSession()
# new_user=User(id='5',name='Bob')
# session.add(new_user)
# session.commit()
# session.close()

#查询
session=DBSession()
user=session.query(User).filter(User.id=='5').one()
print('type:',type(user))
print('name:',user.name)
session.close()