#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   06_upload_fles.py
@Time    :   2019/06/30 10:06:32
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
from tornado.web import RequestHandler
tornado.options.define("port",default=9000,type=int,help="服务器默认监听端口9000")

class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello,Fileupload')



class UploadHandler(RequestHandler):

 
    def post(self):
        '''
        用户上传文件的基本结构
        {
            "form_filename1":[<tornado.httputil.HTTPFile>, <tornado.httputil.HTTPFile>],
            "form_filename2":[<tornado.httputil.HTTPFile>,],        
        }
        form_filename1：post时的keyname

        <tornado.httputil.HTTPFile> 用户上传的文件，包含三个属性
        filename 文件的实际名字（win下含扩展名）
        body:文件体
        content_type 文件类型
        self.request.files["img"][0]["body"]


        '''
        if self.request.files:
            filename=self.request.files['img'][0].filename
            with open(filename,'wb') as f:
                f.write(self.request.files["img"][0]["body"])
            self.write('get File OK')
        else:
            self.write('no files')

if __name__ == "__main__":
    app=tornado.web.Application(
        [
            (r'/',IndexHandler),
            (r'/upfile',UploadHandler)
        ]
        ,debug=True
        ,autoreload=True
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    tornado.ioloop.IOLoop().current().start()
                

