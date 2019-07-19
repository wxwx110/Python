#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   subProcess.py
@Time    :   2019/06/23 16:19:31
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib

import subprocess

#Python代码中运行命令nslookup www.python.org
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


#相当于在命令行执行命令nslookup，然后手动输入
# set q=mx
# python.org
# exit
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)