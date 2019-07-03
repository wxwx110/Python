# here put the import lib
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os

from tornado.web import RequestHandler


tornado.options.define('port',7000,type=int,help='default')


class IndexHandler(RequestHandler):
    
    def get_current_user(self):
        return False

    #使用装饰器，authenticated 进行验证时，必须实现
    # get_current_user()接口 tornado会根据该接口的返回值进行判断
    # 返回false则会跳转到Application定义的login_url 地址
    # 浏览器显示 http://localhost:7000/login?next=%2F
    # next =%2F 其实是next=/意思是，跳转到login之前的所在页面可以在登录后进行处理
    @tornado.web.authenticated
    def get(self):
        nextUrl=self.get_argument("next",'')
        loginStatus=True
        if nextUrl:
            if loginStatus==True:
                self.redirect(nextUrl)
        self.xsrf_token 
        self.render('Index.html')
       
      
    
    def post(self):
        self.write('GetAjaxPost')

class StaticFileHandler(tornado.web.StaticFileHandler):
    """重写StaticFileHandler，构造时触发设置_xsrf Cookie"""
    def __init__(self,*args,**keywargs):
        # 执行父类初始化
        super(StaticFileHandler,self).__init__(*args,**keywargs)
        self.xsrf_token
class LoginUrlHandler(RequestHandler):
    def get(self):
        self.write("login")


if __name__ == "__main__":
    current_path=os.path.dirname(__file__)
  
    app=tornado.web.Application(
        [
          (r'/',IndexHandler)
            ,(r'/login',LoginUrlHandler)
            ,(r'/(.*)',StaticFileHandler,{"path":os.path.join(current_path, "static/html"),"default_filename":"index.html"})
        ]
        ,debug=True
        ,cookie_secret = "2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A="     

        ,xsrf_cookie=True
      
        ,static_path=os.path.join(current_path,'static')

        ,login_url="/login"
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    tornado.ioloop.IOLoop().current().start()