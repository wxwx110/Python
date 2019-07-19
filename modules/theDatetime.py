#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   datetime.py
@Time    :   2019/06/24 16:22:23
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib


from datetime import datetime
#datetime模块还包含一个datetime类
#如果仅导入import datetime，则必须引用全名datetime.datetime
now=datetime.now()
print(now,type(now))

dt=datetime(2015, 4, 19, 12, 20)
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
print (dt,dt.timestamp())

# timespan到时间
t=1429417200.0
print(datetime.fromtimestamp(t))

print('timeFormat',now.strftime('%Y-%m-%d %H:%M:%S'))

from datetime import datetime, timedelta
#时间加减
print(now + timedelta(days=2, hours=12))