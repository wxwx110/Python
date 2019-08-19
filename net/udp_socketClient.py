#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   udp_socketClient.py
@Time    :   2019/06/27 09:45:04
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 指定Udp发送数据时，使用的端口号
# 一般情况下客户端不需要绑定端口
s.bind(('',9898))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    # UDP传输：只保证数据的发送不保证数据的接收
    # 每次发送数据都需要带上IP地址和端口号，
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()