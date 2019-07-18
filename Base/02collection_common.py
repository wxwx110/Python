#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02collection_common.py
@Time    :   2019/07/18 22:09:00
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
'''
运算符	    Python表达式	            结果	                                描述	                      支持的数据类型
+	         [1, 2] + [3, 4]	        [1, 2, 3, 4]	                        合并	                     字符串、列表、元组
*	         'Hi!' * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	         复制	                      字符串、列表、元组
in	          3 in (1, 2, 3)	          True	                                    元素是否存在	         字符串、列表、元组、字典
not in	    4 not in (1, 2, 3)	       True	                                    元素是否不存在	         字符串、列表、元组、字典
'''

'''
序号	                方法	                                描述
1	            cmp(item1, item2)	               比较两个值
2	            len(item)	                             计算容器中元素个数
3	            max(item)	                           返回容器中元素最大值
4	            min(item)	                            返回容器中元素最小值
5	            del(item)	                             删除变量


>>> cmp("hello", "itcast")
-1
>>> cmp("itcast", "hello")
1
>>> cmp("itcast", "itcast")
0
>>> cmp([1, 2], [3, 4])
-1
>>> cmp([1, 2], [1, 1])
1
>>> cmp([1, 2], [1, 2, 3])
-1
>>> cmp({"a":1}, {"b":1})
-1
>>> cmp({"a":2}, {"a":1})
1
>>> cmp({"a":2}, {"a":2, "b":1})
-1

注意：cmp在比较字典数据时，先比较键，再比较值。


'''
# python中对值得传递是引用传递
a=2
b=a
print(a,b)
a=1
print(a,b)
a=[1,2]
b=a
print (a,b)
a.append(5)
print(a,b)
a=[3,4]
print(a,b)