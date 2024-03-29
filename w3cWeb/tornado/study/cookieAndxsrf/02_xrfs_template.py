#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02_xrfs.py
@Time    :   2019/07/02 19:40:25
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
import os

from tornado.web import RequestHandler

tornado.options.define('port',8000,type=int,help='default')

class IndexHandler(RequestHandler):

    def get(self):
        # self.set_secure_cookie('mycookie','value123')
        
        # self.write(r"<form action='c' method='post'><input type='submit' value='sendpost'></form>")
        self.render('Index.html')

class CookieHandler(RequestHandler):
    def get(self):
       pass
    
    def post(self):
       print(self.request.headers["cookie"])
       self.write('get post')

if __name__ == "__main__":
    current_path=os.path.dirname(__file__)
    app=tornado.web.Application(
        [
            (r'/',IndexHandler)
            ,(r'/c',CookieHandler)
        ]
        ,debug=True
        ,cookie_secret = "2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A="
        #打开xsrf_cookie机制
        #POST必须添加token才能被认为是正确的post
        #应用1使用模板网页-form中添加 {% module xsrf_form_html() %}

        ,xsrf_cookie=True
        ,template_path=os.path.join(current_path,'template')
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    tornado.ioloop.IOLoop().current().start()