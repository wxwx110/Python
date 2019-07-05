#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04_async_webapi.py
@Time    :   2019/07/05 09:42:33
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# here put the import lib
import tornado.web
import tornado.ioloop
import json
import asyncio

from tornado.httpclient import AsyncHTTPClient

class IndexHandler(tornado.web.RequestHandler):
    
    @tornado.g
    def on_resonse(resp):
        json_data=resp.body
        data=json.loads(json_data)
        self.write(data.get("city",""))

    # 异步http客户端支持
    @asyncio.coroutine
    def get(self):
        client=AsyncHTTPClient()
        client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=14.132.112.24"
        ,callback=on_resonse)
    

if __name__=='__main__':
    # 注意路由前面的/ 不能省略
    app=tornado.web.Application([(r"/",IndexHandler)])
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()