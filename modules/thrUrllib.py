#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thrUrllib.py
@Time    :   2019/06/26 09:03:21
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
from urllib import request
# 抓取网页信息，因反爬虫暂时不能工作
# headers={
#     'Accept-Language': 'zh-CN',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
# }
# req=  request.Request(url='https://api.douban.com/v2/book/2129650',headers=headers )

# with request.urlopen(req) as f:
#     data=f.read()
#     print('status:',f.status,f.reason)
#     for k,v in f.getheader():
#         print('%s: %s' % (k,v))
#     print('Data:',data.decode('utf-8'))

#  发送get请求
# req=request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# 发送POST请求，Data以byte的形式写入data
from urllib import request, parse

# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# print('login_data:',login_data)
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


#通过代理访问网站
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()

proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass