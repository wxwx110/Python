
# -*- encoding: utf-8 -*-
'''
@File    :   url.py
@Time    :   2019/07/07 09:30:53
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
from handlers import Passport
handlers= [
            (r'/',Passport.IndexHandler)
            
]