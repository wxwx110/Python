#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_cookie.py
@Time    :   2019/07/01 21:30:22
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import tornado.web
import tornado.ioloop
import time

class IndexHandler(tornado.web.RequestHandler):
    # 主页处理类
    def get(self):
        #写cookie
        # 原理 设置cookie实际就是通过设置header的Set-Cookie来实现的。
        #self.set_header("set-cookie","key=value: path=/")
        self.set_cookie("n1", "v1")
       
        self.set_cookie("n3", "v3", expires_days=20)

        #set_cookie默认是用UTC时间，如果要转换成本地时间需要使用mktime()进行转换
        self.set_cookie("n2", "v2", path="/new", expires=time.strptime("2016-11-11 23:59:59","%Y-%m-%d %H:%M:%S"))
        # 利用time.mktime将本地时间转换为UTC标准时间
        self.set_cookie("n4", "v4", expires=time.mktime(time.strptime("2016-11-11 23:59:59","%Y-%m-%d %H:%M:%S")))
        
        #读取cookie
        n3 = self.get_cookie("n3")
        self.write(str(n3))

        #清除cookie
        # clear_cookie(name, path='/', domain=None)
        # 删除名为name，并同时匹配domain和path的cookie。

        # clear_all_cookies(path='/', domain=None)
        # 删除同时匹配domain和path的所有cookie。

        #clear_all_cookies()
        #删除所有cookie

        #执行清除cookie操作后，并不是立即删除了浏览器中的cookie，
        # 而是给cookie值置空，并改变其有效期使其失效。真正的删除cookie是由浏览器去清理的。
        
        self.write("OK")

if __name__=='__main__':
    # 注意路由前面的/ 不能省略
    app=tornado.web.Application(
            [
                (r"/",IndexHandler)
            ]
            #tornado提供了cookie的简单签名加密算法用于防止cookie被修改
            #加密算法：
            #import base64, uuid
            #base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
            #加密cookie的获取和设置
            
            # 设置一个带签名和时间戳的cookie，防止cookie被伪造
            #set_secure_cookie(name, value, expires_days=30)
            
            #获取签名的cookie
            #get_secure_cookie(name, value=None, max_age_days=31)
            # 如果cookie存在且验证通过，返回cookie的值，否则返回None。max_age_day不同于expires_days，
            # expires_days是设置浏览器中cookie的有效期，而max_age_day是过滤安全cookie的时间戳。
            ,cookie_secret = "2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A="
            ,debug=True
        )
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()