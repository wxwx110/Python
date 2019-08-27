#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02_httpserver.py
@Time    :   2019/06/29 20:30:23
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler
import tornado.httpserver

class IndexHandler(RequestHandler):
    def get (self):
        self.write('show me the money')

if __name__ == "__main__":
    app=tornado.web.Application(
        [(r'/',IndexHandler)],
        debug=True
    )

    # app.listen(9000) 简写了http_server绑定和监听的端口设置   
    # app.listen()这个方法只能在单进程模式中使用。 
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(9000)
    tornado.ioloop.IOLoop().current().start()
    '''
        以上是单进程的方式
        多进程方式：

        http_server.bind(9000)
        # http_server.start(num_processes=1)方法指定开启几个进程，
        # 参数num_processes默认值为1
        # 如果num_processes为None或者<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程
        #如果num_processes>0，则创建num_processes个子进程
        http_server.start(0)

        http_server.listen(9000)
        其实是
        http_server.bind(9000)
        http_server.start(1)
        的简写形式

    虽然tornado给我们提供了一次开启多个进程的方法，但是由于：

    每个子进程都会从父进程中复制一份IOLoop实例，如过在创建子进程前我们的代码动了IOLoop实例，那么会影响到每一个子进程，
    势必会干扰到子进程IOLoop的工作；
    所有进程是由一个命令一次开启的，也就无法做到在不停服务的情况下更新代码；
    所有进程共享同一个端口，想要分别单独监控每一个进程就很困难。
    不建议使用这种多进程的方式，而是手动开启多个进程，并且绑定不同的端口。
        



    '''