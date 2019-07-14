#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   BaseHandler.py
@Time    :   2019/07/07 09:47:52
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    @property
    def db(self):
        return self.application.db

    def redis(self):
        return self.application.redis
    
    
    def prepare(self):
        return super().prepare()

    
    def write_error(self, status_code, **kwargs):
        return super().write_error(status_code, **kwargs)

    def set_default_headers(self):
        return super().set_default_headers()
    
    def initialize(self):
        pass
    
    def on_finish(self):
        return super().on_finish()



