#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   file.py
@Time    :   2019/06/21 14:39:56
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib


filepath='D:\\StudyCore\\python\\Senior\\IO\\text.text'
f=open(filepath,'r')

print(f.read())
f.close()
# readlines() 一次读取全部分行显示
# readline() 每次读取一行


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


#读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取      
# 如果在读写文件的过程中，需要从另外一个位置进行操作的话，可以使用seek()
#seek(offset, from)有2个参数
#offset:偏移量
# from:方向
# 0:表示文件开头
# 1:表示当前位置
# 2:表示文件末尾
with open(filepath,'r') as f:
    print( f.read(1),f.tell(),f.read(1),f.tell(),f.read(1),f.tell())
    #使用seek重新定位到文件开头
    f.seek(0,0)    
    print(f.read(1))

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



