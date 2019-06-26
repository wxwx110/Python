#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   xms_sax.py
@Time    :   2019/06/26 10:30:08
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
#操作XML有两种方法：DOM和SAX。
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件。
#正常情况下，优先考虑SAX，因为DOM实在太占内存。
#当SAX解析器读到一个节点时'
#会产生3个事件：
#1、start_element事件,读取开头元素
#2、char_data事件 读取内容
#3、end_element事件 读取结尾元素

from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs:%s' % (name,str(attrs)))
    
    def end_element(self,name):
        print('sax:end_element: %s' %name)
    
    def char_data(self,text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)

#需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，
# 所以需要自己保存起来，在EndElementHandler里面再合并