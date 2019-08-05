#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   extendThread.py
@Time    :   2019/08/03 10:07:23
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import threading 

class Mythread(threading.Thread):

    def run(self):
        print("myThread",self)


a=Mythread()

a.start()
