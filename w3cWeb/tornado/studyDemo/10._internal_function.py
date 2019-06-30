#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10._internal_function.py
@Time    :   2019/06/30 16:45:11
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

class IndexHandler(tornado.web.RequestHandler):

    #每个请求的处理类Handler在构造一个实例后首先执行initialize()方法
    def initialize(self, database):
       self.database = database
    
    #预处理，即在执行对应请求方式的HTTP方法（如get、post等）前先执行，
    # 不论以何种HTTP方式请求，都会执行prepare()方法。
    def prepare(self):
        if self.request.headers.get("Content-Type").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None
    
    #设置默响应头
    def set_default_headers(self):
        print ("执行了set_default_headers()")
        # 设置get与post方式的默认响应体格式为json
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置一个名为itcast、值为python的header
        self.set_header("itcast", "python")

   
    def get(self):    
        self.write('helloWorld')
    
    def post(self):
        if self.json_dict:
            for key, value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key, value))

    def put(self):
        if self.json_dict:
            for key, value in self.json_dict.items():
                self.write("<h3>%s</h3><p>%s</p>" % (key, value))   

     #处理send_error()抛出的错误信息并返回给浏览器错误信息页面。
    def write_error(self, status_code, **kwargs):
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名：%s</p>" % kwargs["title"])
        self.write(u"<p>错误详情：%s</p>" % kwargs["content"])
    
    #在请求处理结束后调用，即在调用HTTP方法后调用。通常该方法用来进行资源清理释放或处理日志等。
    # 注意：请尽量不要在此方法中进行响应输出。
    def on_finish(self):
        print ("调用了on_finish()")
    
   

'''
在正常情况未抛出错误时，调用顺序为：

1、set_defautl_headers()
2、initialize()
3、prepare()
4、处理HTTP方法
5、on_finish()


在有错误抛出时，调用顺序为：
1、set_default_headers()
2、initialize()
3、prepare()
4、处理HTTP方法
5、set_default_headers()
6、write_error()
7、on_finish()
'''

if __name__=='__main__':
    # 注意路由前面的/ 不能省略
    app=tornado.web.Application(
        [
            # 路由的第三个参数可以传入初始化参数给initlize进行Handler的初始化工作
            (r"/",IndexHandler,dict(database="127.0.0.1:3306/dbName"))
        ]
    )
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()