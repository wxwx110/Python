#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   02List.py
@Time    :   2019/06/14 16:35:44
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
# list 可变长的列表,可混合元素
a=[1,2,3,4,5,6,7,8,9,10,'z']
print(a)
# 添加元素
#append 添加一个元素
print ('a.append([\'a\',\'b\',\'c\'])' ,a.append(['a','b','c']),a)

#添加集合逐个元素添加到列表
print("a.extend(['a','b','c'])",a.extend(['a','b','c']),a)

#在指定位置插入元素
print ('a.insert(0,"show")',a.insert(0,'show'),a)


# 删除元素，根据下表
del a[0]
print (a)

#删除最后一个元素 
#pop会返回弹出的元素
print('a.pop()',a.pop(),a)
#可以通过索引指定删除的值
print('a.pop()',a.pop(0),a)

a=[1,1,2,3,4,5,5,6,6]
# 根据指定值，删除元素，但是只删除一个
print('a.remove(1)',a.remove(1),a)

#a.sort(reverse=True)
#排序



print("从索引1开始取到索引2不包含索引2",a[1:2])
print("取前两个元素",a[:2])
print("取后两个元素",a[-2:])
#切片后的list与原来的list不是一个
b=a[:]
b.append('abc')
print("复制组",b,a)





