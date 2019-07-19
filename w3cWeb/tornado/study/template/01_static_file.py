#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_static_file.py
@Time    :   2019/07/01 15:35:43
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
import os

from tornado.web import RequestHandler,StaticFileHandler

# 定义服务器监听端口选项
#限定默认值，数据类型
tornado.options.define("port",default=9000,type=int,help="run server on the given port.")


class IndexHandler(RequestHandler):
    def get(self):     
         self.render('index.html')

if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    print(current_path)
    app=tornado.web.Application(
            [
                #  (r"/",IndexHandler)
                # 提取url地址中127.0.0.1:9000/ 后面的文件映射到 path 路径 下对应的文件，默认是default_filename 定义的文件              
                #注意在os.path.join时只需要输入文件夹名称即可否则会导致报错             
                #r'^/()$' 这样定义正则表达更准确
                #静态资源路由，通常应当放到路由的最后一项，防止拦截到前面的路由
                # api路由通常应当设计成  r'/api/getId'这样的形式
                 (r'/(.*)',StaticFileHandler,{"path":os.path.join(current_path, "static/html"),"default_filename":"index.html"})
            ]
            ,debug=True
            ,reload=False
            # sys.path 指的是PYTHO解析器路径clrea
            #os.path值的是操作系统的路径

            # 通过本参数配置系统静态文件的路径
            #定义后通过http://127.0.0.1:9000/static/html/index.html路径进行访问
            #注意/static 与当前文件所在的文件夹static并没有任何关联关系，static是tornado的默认命名访问路径
            # 为了配合nginx 的部署静态文件夹所在文件最好命名成static
             ,static_path=os.path.join(current_path, "static")        
        )
  
    # print('join path:',os.path.dirname(__file__).join("statics"))
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop().current().start()


