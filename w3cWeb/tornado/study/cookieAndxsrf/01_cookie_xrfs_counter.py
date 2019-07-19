#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_cookie_xrfs.py
@Time    :   2019/07/02 19:23:10
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

tornado.options.define('port',9000,type=int,help='default')



class IndexHandler(RequestHandler):
    def get(self):
        # 通过http://127.0.0.1:8000/?f=9000/端口访问实现了对COOKIE的计数增加
        self.write('<html><head><title>被攻击的网站</title></head>'
        '<body><h1>此网站的图片链接被修改了</h1>'
        '<img alt="这应该是图片" src="http://127.0.0.1:8000/?f=9000/">'
        '</body></html>'
        )

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
