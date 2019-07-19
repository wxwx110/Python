#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_static_file.py
@Time    :   2019/07/01 15:35:43
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
import os

from tornado.web import RequestHandler,StaticFileHandler

# 定义服务器监听端口选项
#限定默认值，数据类型
tornado.options.define("port",default=9000,type=int,help="run server on the given port.")


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html',price1=100,price2=200,fileName="abcde")
        

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
   
    app=tornado.web.Application(
            [
                 (r"/",IndexHandler)
             
            ]
            ,debug=True
            ,reload=False
         
             ,static_path=os.path.join(current_path, "static")

            #定义模板文件路径
             ,template_path=os.path.join(current_path, "template")
        )
  
    # print('join path:',os.path.dirname(__file__).join("statics"))
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop().current().start()


