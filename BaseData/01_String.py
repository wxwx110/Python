#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_String.py
@Time    :   2019/07/17 22:01:22
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib

a="abcdef"
# 字符串是一个iterable
for x in a:
    print(x)
#可以通过下标查询
print(a[0],a[1],a[2])

# 切片的语法：[起始:结束:步长]
# 起始、结束、补偿可以为+ 或者 -
# 起始、结束为负表示从字符串的末尾往前的下表
# 结束位置不包含再切片范围内
# 步长为负，表示截取的方向从右往左
print ('a=',a)
print('a[1:3]=',a[1:3])
print('a[-2:]',a[-2:])
print('a[-2::-1]',a[-2::-1])

print ("a[1:5:2]",a[1:5:2])
# 不满足时返回空字符串
print ("a[1:5:-2]",a[1:5:-2],type(a[1:5:-2]))

print ("a[-5:-1]",a[-5:-1])

# f反转字符串
print(a[::-1])

# mystr.find(str, start=0, end=len(mystr))
# 检测 str 是否包含在 mystr中，从左边开始查找如果是返回开始的索引值，否则返回-1
# mystr.rfind(str, start=0,end=len(mystr) )
#从右边查找

# mystr.index(str, start=0, end=len(mystr)) 
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常
#mystr.rindex( str, start=0,end=len(mystr))
#从右查找

# mystr.count(str, start=0, end=len(mystr))
#  str在start和end之间 在 mystr里面出现的次数

# mystr.replace(str1, str2,  mystr.count(str1))
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

# mystr.split(str=" ", 2)   
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
a="a|b|c|c|d|e"
print('a.split(\'|\',2)',a.split('|',2))
#splitlines
#按照行进行分割
a="hello \n world"
print('a.splitlines()',a.splitlines())
#partition
#把mystr以str分割成三部分,str前，str和str后
#rpartition
# 从右开始切割



# mystr.capitalize()
#把字符串的第一个字符大写

#title()
#把字符串的每个单词首字母大写

#startswith
# 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False

#endswith
#检查字符串是否以obj结束，如果是返回True,否则返回 False.

#ljust
#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
a="hello"
print(a.ljust(10,'^'))
#rjust
#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
#center
#中间对齐

#lstrip 删除左边空格
#rstrip 删除右边空格
#strip 删除两端空格

#isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False

#isdigit
#如果 mystr 只包含数字则返回 True 否则返回 False.

#isalnum
#如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False

#isspace
#如果 mystr 中只包含空格，则返回 True，否则返回 False.

#mystr.join(str)
#join(iterable)
# 再给定的字符串数组后面插入前面的字符串，并返回一个新的字符串
a=" "
b=["show","me","the","money"]
print(a.join(b))

a="show me the money"

b="_"
print(b.join(a))
