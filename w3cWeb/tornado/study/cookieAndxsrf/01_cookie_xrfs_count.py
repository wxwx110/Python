#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_cookie_count.py
@Time    :   2019/07/02 15:17:39
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

from tornado.web import RequestHandler

tornado.options.define('port',8000,type=int,help='default')

class IndexHandler(RequestHandler):

    def get(self):
        countCookieValue=1
       
    #    为了保护信息安全，应该在post中对cookie进行处理
        if self.get_cookie('count_cookie'):
            countCookieValue=int(self.get_cookie('count_cookie'))+1
            print (countCookieValue)
        self.set_cookie('count_cookie',str(countCookieValue))

        self.write('you have visited our Web %s times' % countCookieValue)

if __name__ == "__main__":
    app=tornado.web.Application(
        [
            (r'/',IndexHandler)
        ]
        ,debug=True
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    tornado.ioloop.IOLoop().current().start()
