#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theTurtle3.py
@Time    :   2019/06/26 22:25:05
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
from turtle import *

# # 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()

import random

def gogo(): 
    colormode(255)
    width(2) 
    for i in range(200): 
        r=int(random.uniform(0,255)) 
        g=int(random.uniform(0,255)) 
        b=int(random.uniform(0,255)) 
        fd(100) 
        if(i%2==0): 
            pencolor(r,g,b) 
            rt(155) 
        else: 
            pencolor(r,g,b) 
            lt(100)
    done()

gogo()