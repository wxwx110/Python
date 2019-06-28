#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theWSGI.py
@Time    :   2019/06/27 16:54:36
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# Python内置WSGI服务器，wsgiref

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    print(environ['PATH_INFO'])
    return [body.encode('utf-8')]
'''
#扩展
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    # 响应get请求
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    #响应post请求
    if method=='POST' and path='/signin':
        return handle_signin(environ, start_response)
    ...
'''

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 浏览器打开 http://localhost:8000/  既可以访问