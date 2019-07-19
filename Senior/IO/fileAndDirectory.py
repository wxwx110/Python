#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fileAndDirectory.py
@Time    :   2019/06/22 16:16:29
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import os
print(os.name)  
# 环境变量
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
# print(os.environ)  

#获取当前路径
print (os.path.abspath('.'))

#创建目录 -使用相对路径，相对当前路径下的目录
# os.mkdir('ttaa')

#移除目录
#os.rmdir('ttaa')


# os.path.join('.','aabb')
#创建目录为保证系统兼容性使用os.path.join进行目录连接会根据操作系统返回对应的路径
path=os.path.join('.','aabb')
#os.mkdir(path)

#split与join同理
print('pathsplit',os.path.split(path))

#os.path.splitext()可以直接让你得到文件扩展名

print(os.path.splitext(r"D:\StudyCore\python\Senior\IO\fileAndDirectory.py"))

# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')

# os 未提供复制文件函数 shutil模块提供了copyfile()的函数
# import shutil

# shutil.copyfile('aabbcc.text',os.path.abspath('aabb'))

#列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

#要列当前出所有的.py文件，
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
