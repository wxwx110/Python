#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07_get_ajax.py
@Time    :   2019/06/30 14:32:49
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
from tornado.web import RequestHandler

tornado.options.define("port",default=9000,type=int,help='server default port')

class IndexHandler(RequestHandler):
    def get(self):
        self.write('helloAjax')

class AjaxHandler(RequestHandler):

    def post(self):
        print (self.request.headers)
        print(self.request.body)
        #self.get_argument("a","NONEvalue")无法获取ajax数据
        #getValue=self.get_argument("a","NONEvalue")
        getValue='aaa'
        if self.request.headers.get('Content-Type').startswith('application/json'):          
            getValue=json.loads(self.request.body)
        self.write(getValue["a"])

if __name__ == "__main__":
    app=tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/ajaxdata',AjaxHandler)
        ]
        ,debug=True
    )
    htt_server=tornado.httpserver.HTTPServer(app)
    htt_server.bind(tornado.options.options.port)
    htt_server.start(1)
    tornado.ioloop.IOLoop().current().start()