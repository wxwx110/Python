#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tcpip.py
@Time    :   2019/06/27 08:45:04
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import socket
#服务器绑定UDP端口和TCP端口互不冲突


#创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com',80))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer=[]
while True:
    # 每次最多接收1024个字节
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
#关闭连接
s.close()

data=b''.join(buffer)
print(data)

# 分离http请求头和网页
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
