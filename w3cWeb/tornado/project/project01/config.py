#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2019/07/07 15:14:21
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   系统配置文件
'''

# here put the import lib

import os

# Application配置参数
settings={
     "static_path":os.path.join(os.path.dirname(__file__),"static")
     ,"template_path":os.path.join(os.path.dirname(__file__),'template')
     ,"debug":True
     ,"cookie_secret":"kFt1p488QMegs5vXh+Zm3ULrUK3rl0b8kKjdbSjvoqc="
     ,"xsrf_cookies":True
     ,"debug":True
}

# Application配置参数



# 数据库配置参数
mysql_options = dict(
    host="127.0.0.1",
    database="ihome",
    user="root",
    password="mysql"
)

# Redis配置参数
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# 日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/log")
#日志级别 debug|info|warning|error
log_level = "debug"

# 密码加密密钥
passwd_hash_key = "nlgCjaTXQX2jpupQFQLoQo5N4OkEmkeHsHD9+BBx2WQ="