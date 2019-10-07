#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04_app.py
@Time    :   2019/06/29 15:46:47
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

from tornado.options import define,options
from tornado.web import RequestHandler,url

tornado.options.define('port',type=int,default=9000,help='WebServerPort')

class IndexHandler(RequestHandler):

    def get(self):
        # reverse_url()获取命名url
        self.write('<a href="'+self.reverse_url('cpp_url')+'">cpplink</a>')

class SubjectHandler(RequestHandler):
    # 接收路由中定义的字典{"subject":"python"}，对handler进行初始化
    def initialize(self,subject):
        self.subject=subject
       

    def get(self):
        self.write(self.subject)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        [
            #路由中的字典，会传入到对应的RequestHandler的initialize()方法中
            (r"/",IndexHandler),
            (r"/python",SubjectHandler,{"subject":"python"}),
            # 使用name别名，时不能使用tuple需要使用tornado.web.url()函数
            #可以调用RequestHandler.reverse_url(name)获取url
            url(r"/cpp",SubjectHandler,{"subject":"cpp"},name="cpp_url")
        ],
        #debug=True 后，tornado会工作在调试/开发模式
        debug=True
        #再开发模式下可使用如下特性
        #自动重启代码修改后自动重启服务，如果修改的代码出错，则需要手动重启
        ,autoreload=True

        #取消缓存编译的模板
        ,compiled_template_cache=False

        #取消缓存静态文件hash值
        ,static_hash_cache=False

        #提供追踪信息,当RequestHandler或者其子类抛出一个异常而未被捕获后，会生成一个包含追踪信息的页面
        ,serve_traceback=True

    )
    
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()