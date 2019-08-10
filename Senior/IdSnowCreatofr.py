#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   IdSnowCreator.py
@Time    :   2019/08/09 18:31:43
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
'''雪花算法用于生成数据库主键id

算法描述：

最高位是符号位，始终为0，不可用。
41位的时间序列，精确到毫秒级，41位的长度可以使用69年。时间位还有一个很重要的作用是可以根据时间进行排序。
10位的机器标识，10位的长度最多支持部署1024个节点。
12位的计数序列号，序列号即一系列的自增id，可以支持同一节点同一毫秒生成多个ID序号，12位的计数序列号支持每个节点每毫秒产生4096个ID序号。


'''
import time
class Snow(object):
 
    def __init__(self, idx=None):
        init_date = time.strptime('2010-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")
        self.start = int(time.mktime(init_date))
        self.last = int(time.time())
        self.count_id = 0
        self.idx = idx if idx else 0
 
    def get(self):
        now = int(time.time())
        temp = now - self.start
        if len(str(temp)) < 9:
            length = len(str(temp))
            s = '0' * (9 - length)
            temp = s + str(temp)
        if now == self.last:
            self.count_id += 1
        else:
            self.count_id = 0
            self.last = now
        if len(str(self.idx)) < 2:
            length = len(str(self.idx))
            s = '0' * (2 - length)
            self.idx = s + str(self.idx)
        if self.count_id == 99999:
            time.sleep(1)
        count_id_data = str(self.count_id)
        if len(count_id_data) < 5:
            length = len(count_id_data)
            s = '0' * (5 - length)
            count_id_data = s + count_id_data
        return ''.join([str(temp), self.idx, count_id_data])
 
 
if __name__ == '__main__':
    import threading
    snow = Snow('001')
 
    def echo():
        print(snow.get())
 
    threads = [threading.Thread(target=echo) for i in range(100)]
  
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # threads =threading.Thread(target=echo)
    # threads.start()
