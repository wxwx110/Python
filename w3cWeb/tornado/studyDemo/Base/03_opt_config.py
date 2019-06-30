# conding:utf-8
'''
使用配置文件的时候，通常会新建一个python文件（如config.py），
然后在里面直接定义python类型的变量（可以是字典类型）；
在需要配置文件参数的地方，
将config.py作为模块导入，并使用其中的变量参数。
'''
# Redis配置
redis_options = {
    'redis_host':'127.0.0.1',
    'redis_port':6379,
    'redis_pass':'',
}

# Tornado app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies':False,
    'login_url':'/login',
    'debug':True,
}

# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
'''
使用 config.py的模块
import tornado.web
import config

if __name__ = "__main__":
    app = tornado.web.Application([], **config.settings)
'''