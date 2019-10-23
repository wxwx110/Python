
# -*- encoding: utf-8 -*-
'''
@File    :   server.py
@Time    :   2019/07/06 08:39:31
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   启动服务
'''

# here put the import lib
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
import config


import torndb

from tornado.options import options, define

from urls import handlers
define('port' ,type=int,default=9000,help='run server on the given port')


class Application(tornado.web.Application):

    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        # 声明配置数据库初始化参数
        #数据库mysql配置
        self.db = torndb.Connection(**config.mysql_options)
        #数据库Redis配置
        self.redis = redis.StrictRedis(**config.redis_options)


def main():
    #命令行执行python server.py --help可以查看命令行相关配置信息
    # log_file_max_size -单日志文件最大体积，超出后会创建新的文件
    # log_file_num_backups -文件保存数量
    # log_file_prefix -文件路径
    # log_rotate-interval 文件书写间隔
    # log_rotate-mode 日志文件保存方式：时间time，（默认）大小size
    # log_rotate-when 日期模式，文件保存时间类型 年月日天等
    # linux下可以使用tail -f log 实时查看关注日志文件 
    # 定义日志书写路径
    # 注意该路径和文件并不会默认创建，需要手创建
    options.log_file_prefix = config.log_path
    # 定义日志记录级别
    options.logging = config.log_level

    tornado.options.parse_command_line()
    app=tornado.web.Application(
        handlers
       ,**config.settings
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start()
    print('server start')
    tornado.ioloop.IOLoop().current().start()

if __name__ == "__main__":
    main()