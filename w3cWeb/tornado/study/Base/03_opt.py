#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   03_opt.py
@Time    :   2019/06/29 21:12:38
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

# 定义服务器监听端口选项
#限定默认值，数据类型
tornado.options.define("port",default=9000,type=int,help="run server on the given port.")

# 无意义，演示多值情况
tornado.options.define("itcast",default=[],type=str,multiple=True,help="itcast subjects")

class IndexHandler(RequestHandler):
    def get(self):
        self.write('helloWorld')

if __name__ == "__main__":
    #通过配置文件加载配置信息
    #注意，再使用文件加载时，不能省略
    #tornado.options.define("port",default=9000,type=int,help="run server on the given port.")
    #tornado.options.define("itcast",default=[],type=str,multiple=True,help="itcast subjects")
    # 的相关定义，否则读取文件时会报错Unrecognized option ，因为tornado不知道你加载的是什么配置

    tornado.options.parse_config_file(r"D:\StudyCore\python\w3cWeb\tornado\studyDemo\03optConfig")


    #通过加入命令行参数 --help　可以查看所有选项变量的信息
    '''
    调用parse_command_line()或者parse_config_file()的方法时，
    tornado会默认为我们配置标准logging模块，
    即默认开启了日志功能，并向标准输出（屏幕）打印日志信息。
    from tornado.options import options, parse_command_line
    options.logging = None
    tornado.options.parse_command_line()
    '''
    # tornado.options.parse_command_line() 命令行输入 --help 运行参数时，
    # 会显示定义的options定义的help信息,同时能够接收命令行参数作为程序的启动配置
    tornado.options.parse_command_line()
    print(tornado.options.options)
    print (tornado.options.options.itcast)
    app=tornado.web.Application(
            [
                (r"/",IndexHandler)
            ]
        )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop().current().start()

    #python opt.py --port=9000 --itcast=python,c++,java,php,ios
