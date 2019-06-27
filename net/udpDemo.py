#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   udpDemo.py
@Time    :   2019/06/27 09:56:38
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

import socket  ,threading  #引入套接字


def udp_send(udp_socket):

    while True:
        num1 = '127.0.0.1'
        num2 = 9997
        send_data = input('请输入要发送的数据：')
        send_data = send_data.encode('utf-8')
        udp_socket.sendto(send_data,(num1,num2))  #sendto（发送数据，发送地址）

def udp_recv(udp_socket):
    while True:
        recv_data = udp_socket.recv(1024)
        recv_data = recv_data.decode('utf-8')
        print('收到信息为:%s'%recv_data)

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #创建套接字
    ip = '127.0.0.1'                                           #服务器ip和端口
    port = 9997
    udp_socket.bind((ip,port))                                   #服务器绑定ip和端口
    #发送数据
    t=threading.Thread(target=udp_send,args=(udp_socket,))     # Thread函数用于并行
    #接收数据
    t1=threading.Thread(target=udp_recv,args=(udp_socket,))
    t.start()                                                 #并行开始
    t1.start()

if __name__ == '__main__':
    main()
