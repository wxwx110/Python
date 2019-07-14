#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   session.py
@Time    :   2019/07/13 09:33:10
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# session=Session(request_handler)
# session.sid
# session.data
import uuid
import logging
import json
import constants

# 调用
# control层 self是HttpHandler的基类
#session=Session(request_handler=self)
# session.session_id=uuid4().get_hex()
#session.data=第一次访问或者出错{} 否则，是json.loads()反序列化的对象

class Session(object):
    # 通过requesthandler获取cookie创建session
    def __init__(self, request_handler, ):
        self.request_handler=request_handler
        # 判断是否已经存在session
        self.session_id=self.request_handler.get_secure_cookie("session_id")

        if not self.session_id:
            # 用户第一次访问，生成一个session_id,全局唯一
            self.session_id=uuid.uuid4().get_hex()
            self.data={}
        else:
            # 如果已经存在则直接从redis中取
            try:
                data=self.redis.get("sess_%s" % self.session_id)
            except Exception as e:
                logging.error(e)
                self.data={}
            if not data:
                self.data={}
            else:
                # 构建时使用json序列化到Redis中
                # 取用时再将data反序列化 成对象 
                self.data=json.loads(self.data)
        
        # 保存session
    def save(self):
        json_data=json.dumps(self.data)
        try:
            # 保存到数据库并设置超时时间
            self.redis.setex("sess_%s" %self.session_id,constants.SESSION_EXPIRES_SECONDS,json_data)
        except Exception as e:
            logging.error(e)
            raise Exception('save session faild')
        else:
            self.request_handler.set_secure_cookie('session_id',self.session_id)

    # 清理session
    def clear(self):
        self.request_handler.clear_cookie("session_id")
        try:
            self.redis.delete("sess_%s" %self.session_id )
        except Exception as e:
            logging.error(e)





