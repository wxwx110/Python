#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   udp_chartRoomServer.py
@Time    :   2019/08/16 08:38:18
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
from threading import Thread
import time,socket

udpchannl=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpchannl.bind(('',9997))

addr=('',0)

def reciveMessage():
    global addr
    while True:
        data,addr=udpchannl.recvfrom(1024)
        print(">>time:%s data:%s" %(time.time(),data) )
   



def sendMessage():
    while True:
        sendInfo=input("<<")
        print (addr)
        # udpchannl.sendto(sendInfo.encode("utf-8"),addr)
        

if __name__ == "__main__":  
    print("CHART server start %s" %time.time())
    threadrecive=Thread(target=reciveMessage,)
    threadsendMessage=Thread(target=sendMessage)
    threadrecive.start()
    threadsendMessage.start()

    threadrecive.join()
    threadsendMessage.join()


    print("chart server closeed")
    
