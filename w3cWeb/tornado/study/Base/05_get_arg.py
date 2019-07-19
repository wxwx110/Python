#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   05_get_arg.py
@Time    :   2019/06/29 16:33:02
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    
    def get(self):
        # get_query_argument(name, default=_ARG_DEFAULT, strip=True)
        # name 参数值
        # default-如果没有获得改参数返回的默认值，如果不设置会抛出tornado.web.MissingArgumentError异常
        # strip-是否过滤参数值的空格
        queryParam1=self.get_query_argument("param1")
       
        
        #get_query_arguments(name, strip=True)
         # 使用get_arguments可以截取所有名称未param2的参数值，并返回一个list
        #http://localhost:9000/?param1=900&param2=300&param2=500
        queryParam2=self.get_arguments("param2")

        #get_query_argument 截取重名参数时智能获取最后一个值 500
        queryParam3=self.get_query_argument("param2")
        self.write("param1:%s \n param2:%s \n param3:%s" % (queryParam1,queryParam2,queryParam3))

        # POST发送参数的获取，与 queryParam一致 
        # 对于请求体数据为json或xml的，无法通过这两个方法获取
        
        # get_body_argument(name, default=_ARG_DEFAULT, strip=True)
        # bodyParam1=self.get_body_argument("param1")
        
        # get_body_arguments(name, strip=True)
        # bodyParam2=self.get_body_arguments("param2")

        #
        # self.get_argument
        # self.get_arguments
        # 以上两个函数不区分queryparam还是bodyparam 但是由于queryUrl先解析 body后解析，
        # 当出现重名参数时，self.get_argument获取的是最后一个body的参数值

        

if __name__ == "__main__":
    app=tornado.web.Application(
        [(r'/',IndexHandler)],
        debug=True
    )
    app.listen(9000)
    tornado.ioloop.IOLoop().current().start()


