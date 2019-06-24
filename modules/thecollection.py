#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thecollection.py
@Time    :   2019/06/24 20:17:22
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
from collections import namedtuple
#1 不可变集合
a=(1,2)
print(a,a[0],a[1])

#2 命名的不可变集合，可以使用 名字.属性，进行访问，只读
Point =namedtuple('Point',['x','y'])
p=Point(1,2)
print(p,p.x,p.y)

#3 列表，索引访问快速，但插入，删除元素较慢
a=[1,2,3,4]

# 4 双向列表 ，插入删除速度较快
from collections import deque
q=deque(['a','b',1])
q.append('c')
q.appendleft('z')
print (q)
q.popleft()
print (q)

from collections import defaultdict
# 自定义空字典返回值
dd=defaultdict(lambda : 'NOKEY')
dd['key1']='kkkk'
print(dd['key1'],dd['key2'])

# 5 有序的dict,根据插入的顺序进行排序而不是key的顺序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])


od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d,od)

# 6 ChainMap可以把一组dict串起来并组成一个逻辑上的dict

from collections import ChainMap
aParam={'a':1}
bParam={'b':3}
defaultParam={'a':9,'b':9,'c':9}
cm1=ChainMap(aParam,defaultParam)
cm2=ChainMap(bParam,defaultParam)
cm3=ChainMap(aParam,bParam,defaultParam)
print('cm1:',cm1['a'],cm1['b'],cm1['c'])
print('cm2:',cm2['a'],cm2['b'],cm2['c'])
print('cm3:',cm3['a'],cm3['b'],cm3['c'])

# 7 counter
from collections import Counter

c=Counter()
for x in 'showmethemoney':
    c[x]=c[x]+1
print(c)



