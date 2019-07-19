#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01.py
@Time    :   2019/06/28 16:57:27
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
''' 

# here put the import lib
import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    # 主页处理类
    def get(self):
    
        self.write('helloWorld')

if __name__=='__main__':
    # 注意路由前面的/ 不能省略
    app=tornado.web.Application([(r"/",IndexHandler)])
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()