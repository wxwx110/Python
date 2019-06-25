#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theBase64.py
@Time    :   2019/06/25 08:46:50
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
#Base64的原理准备一个包含64个字符的数组：['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
#对二进制数据进行处理，每3个字节一组，一共是3x8=24bit
#划为4组，每组6个bit
#然后查表，获得相应的4个字符，就是编码后的字符串
#Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%编码后的文本数据可以在邮件正文、网页等直接显示
#编码的二进制数据不是3的倍数，最后会剩下1个或2个字节
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号

import base64
a=b'a'
print(base64.b64encode(a))



# url 中处理 不能把+和/ 作为参数使用 字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')))
#=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
#因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
# 因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。