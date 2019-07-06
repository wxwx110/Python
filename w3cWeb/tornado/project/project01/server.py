#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2019/07/06 08:39:31
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver

import os

def main():
    app=tornado.web.Application(
        [
            (r'/',IndexHandler)
            
        ]
       ,debug=True
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start()


if __name__ == "__main__":
    main()