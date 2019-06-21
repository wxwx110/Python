#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   20debugUnitTest.py
@Time    :   2019/06/21 10:29:38
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    
    def __getattr__(self,key):
        try:
            #return int(self[key])+1
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s' " %key)
    
    def __setattr__(self ,key ,value):
        self[key]=value


import unittest

class TestDic(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    
    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d['key'],'value')

    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
    
    def test_keyerror(self):
        d=Dict()
        #期待抛出指定类型的Error
        with self.assertRaises(KeyError):
            value=d['empty']

    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty
    #setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

#运行单元测试
if __name__ == '__main__':
    unittest.main()


