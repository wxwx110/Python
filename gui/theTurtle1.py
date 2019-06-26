#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   theturtle.py
@Time    :   2019/06/26 22:20:56
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 风蓝科技
@Desc    :   None
'''

# here put the import lib
from turtle import *

# 设置笔刷宽度:
width(4)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()