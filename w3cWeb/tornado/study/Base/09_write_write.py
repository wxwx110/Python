#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   08_write_write.py
@Time    :   2019/06/30 15:39:18
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import json

from tornado.web import RequestHandler

tornado.options.define("port",default=9000,type=int,help='show me the money')
class IndexHandler(RequestHandler):
    # 该方法会在进入HTTP处理方法前先被调用，可以重写此方法来预先设置默认的headers
    #在HTTP处理方法中使用set_header()方法会覆盖掉在set_default_headers()方法中设置的同名header。
    def set_default_headers(self):
        print ("执行了set_default_headers()")
        # 设置get与post方式的默认响应体格式为json
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置一个名为itcast、值为python的header
        self.set_header("itcast", "python")
        
    def get(self):
        '''
            write方法是写到缓冲区的
            可以多次写入后再整体输出
        '''
        self.write("show")
        self.write("me")
        self.write("the")
        self.write("money")

        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        # 写入json
        #自己手动序列化时为Content-Type:text/html; charset=UTF-8，
        # write方法时为Content-Type:application/json; charset=UTF-8
        # 方法1先处成文本
        stu_json = json.dumps(stu)
        # self.write(stu_json)
        # 方法2
        # 当write方法检测到我们传入的chunk参数是字典类型后，会自动帮我们转换为json字符串。
        self.write(stu)

class Err404Handler(RequestHandler):
    """对应/err/404"""
    def get(self):
        self.write("hello itcast")
        self.set_status(404) # 标准状态码，不用设置reason

class Err210Handler(RequestHandler):
    """对应/err/210"""
    def get(self):
        self.write("hello itcast")
        self.set_status(210, "itcast error") # 非标准状态码，设置了reason

class Err211Handler(RequestHandler):
    """对应/err/211"""
    def get(self):
        self.write("hello itcast")
        self.set_status(211) # 非标准状态码，未设置reason，错误

class LoginHandler(RequestHandler):
    """对应/login"""
    def get(self):
        self.write('<form method="post"><input type="submit" value="登陆"></form>')

    def post(self):
        #页面重定向
        self.redirect("/")

# send_error(status_code=500, **kwargs)
#抛出HTTP错误状态码status_code，默认为500，kwargs为可变命名参数。
# 使用send_error抛出错误后tornado会调用write_error()方法进行处理，
# 并返回给浏览器处理后的错误页面 后续的相关操作无效
class SendErroHandler(RequestHandler):
    def get(self):
        self.write("主页")
        self.send_error(404, content="出现404错误")
        # send_error后，后续处理无效
        self.write('errinfo')

# write_error(status_code, **kwargs)
#处理send_error抛出的错误信息并返回给浏览器错误信息页面。
# 可以重写此方法来定制自己的错误显示页面。
class WriteErroHandler(RequestHandler):
    def get(self):
        err_code = self.get_argument("code", None) # 注意返回的是unicode字符串，下同
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        if err_code:
            self.send_error(err_code, title=err_title, content=err_content)
        else:
            self.write("主页")

    def write_error(self, status_code, **kwargs):
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名：%s</p>" % kwargs["title"])
        self.write(u"<p>错误详情：%s</p>" % kwargs["content"])
        

if __name__ == "__main__":
    app=tornado.web.Application(
        [
            (r'/',IndexHandler)
            ,(r'/err211',Err211Handler)
            ,(r'/err210',Err210Handler)
            ,(r'/err404',Err404Handler)
            ,(r'/senderr',SendErroHandler)
            ,(r'/writeerro',WriteErroHandler)
            ,(r'/redirect',LoginHandler)
        ]
        ,debug=True
    )

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start()
    tornado.ioloop.IOLoop().current().start()
