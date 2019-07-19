#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07_get_arg_regular.py
@Time    :   2019/06/30 11:52:55
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler

define("port", default=9000, type=int, help="run server on the given port.")

class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello itcast.")

class SubjectCityHandler(RequestHandler):
    def get(self, subject, city):
        self.write(("Subject: %s<br/>City: %s" % (subject, city)))

class SubjectDateHandler(RequestHandler):
    def get(self, date, subject):
        self.write(("Date: %s<br/>Subject: %s" % (date, subject)))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        # 当访问路由不匹配时 404
         # 无名方式
        #  解析后的参数按照顺序写入处理函数
        (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),
        # 命名方式，
        # 指定参数的位置 解析后对处理
        (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)", SubjectDateHandler), 
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    
    tornado.ioloop.IOLoop.current().start()