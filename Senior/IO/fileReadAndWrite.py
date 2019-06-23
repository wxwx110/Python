#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file.py
@Time    :   2019/06/21 14:39:56
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib


filepath='D:\\StudyCore\\python\\Senior\\IO\\text.text'
f=open(filepath,'r')

print(f.read())
f.close()


try:
    f = open(filepath, 'r')
    print(f.read())
finally:
    if f:
        f.close()

# with简写，等同上面的内容
with open(filepath, 'r') as f:
    #读取默认类型是str
    print(type(f.read()))
    print(f.read())
print('_____________________')

with open(filepath,'r') as f:
    a=0
    #在文件大小不确定的情况下，按照一定的 size读取文件
    for x in f.read(5):
        a=a+1
        print(str(a)+x+'|')

# 包含中文时，要加上第三个参数encoding='utf-8'
with open(filepath,'r',encoding='utf-8') as f:
    # readlines按行读取文件
    for x in f.readlines():
        # 去除回车
        print (x.strip())

#读取图片
# f = open('/Users/michael/test.jpg', 'rb') 
#根据指定字节码读取文件
#f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
#遇到不规范字符过滤
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 当不写文件路径时，默认路径是当前文件所在目录的根目录上？
with open ("aabbcc.text",'w' ,encoding='utf-8') as f:
    f.write("我爱中国人")
    f.write("i love china")



