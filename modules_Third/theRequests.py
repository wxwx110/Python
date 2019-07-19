#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theRequests.py
@Time    :   2019/06/26 20:56:43
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import requests
# r=requests.get('https://www.douban.com')
# print(r.status_code)
# print (r.text)

#带参数请求
 
r=requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
#requests自动检测编码
print(r.encoding)
#无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象
# print(r.content)

#直接获取json
# r = requests.get('https://mirrors.tuna.tsinghua.edu.cn/static/status/isoinfo.json')
# print(r.json())

#传入head
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print (r.text)


#post 请求
#默认使用application/x-www-form-urlencoded对POST数据编码
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON

#文件上传 ，简化成file参数
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)


#写cookie
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)

#设置超时
#r = requests.get(url, timeout=2.5) 
#把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。
#r.headers 获取响应头
#Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
#r.headers['Content-Type']
#'text/html; charset=utf-8'

