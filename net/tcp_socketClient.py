#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tcpip_socketClient.py
@Time    :   2019/06/27 09:34:23
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    # TCP发送数据，只需要事先建立连接通道，发送数据时候
    # 可以不带地址和端口号
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()