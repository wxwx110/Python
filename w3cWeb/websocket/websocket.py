#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   websocket.py
@Time    :   2019/07/05 10:52:42
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
import os
import datetime

from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.websocket import WebSocketHandler

define("port", default=9000, type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render("webchart.html")

class ChatHandler(WebSocketHandler):
    # 用来存放在线用户的容器,所有handler共享
    users = set()  

    # 当一个websocket被建立时调用
    def open(self):
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:  # 向已在线用户发送消息

            # 向客户端发送消息messagea，message可以是字符串或字典（字典会被转为json字符串）
            # 若binary为False，则message以utf8编码发送；二进制模式（binary=True）时，可发送任何字节码
            u.write_message(u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    # 当客户端发送消息message过来时被调用，注意此方法必须被重写
    def on_message(self, message):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(u"[%s]-[%s]-说：%s" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    #当WebSocket连接关闭后被调用
    def on_close(self):
        self.users.remove(self) # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message(u"[%s]-[%s]-离开聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
   
    #判断源origin，对于符合条件（返回判断结果为True）的请求源origin允许其连接，否则返回403
    def check_origin(self, origin):
        # 允许WebSocket的跨域请求默认情况下不允许
        # 设置未true后可以允许同IP的客户端连接访问服务器
        return True  

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
            (r"/", IndexHandler),
            (r"/chat", ChatHandler),
        ],
        static_path = os.path.join(os.path.dirname(__file__), "static"),
        template_path = os.path.join(os.path.dirname(__file__), "template"),
        debug = True
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()