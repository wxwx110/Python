#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02collection_dictionary.py
@Time    :   2019/07/18 21:43:40
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

info={'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

# 使用get获取不存在元素时返回Null,使用【】方式访问不存在字典时会报错
print(info['name'],info.get('name'),info.get('abc'))

# 对不存在字典进行复制时，会自动添加改元素
# 如果存在，则修改该字典值
info['aa']=123
print(info)

# 删除字典值
del info['aa']

# 清空字典中的内容
# info.clear()
# print('info after clear',info)

#删除字典
# del info
# print(info)

#返回字典中键值对的个数
print('len(info)',len(info))

# 返回字典中的keys list对象
print('info.keys()',info.keys())

# 返回字典中的Values list对象
print('info.values()',info.values())

#以list +tuple的方式返回k-v对
print (info.items())

# 根据item进行遍历
for key,value in info.items():
    print ('%s-%s' % (key,value))

# enumerate 返回一个枚举 可以产生一个带索引的序列
for i ,item in enumerate(info.items()):
    print (i,item)


