#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thePsutil.py
@Time    :   2019/06/26 21:42:05
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# here put the import lib
import psutil
# #CPU逻辑核心
# print(psutil.cpu_count())
# #CPU物理核心数
# print(psutil.cpu_count(logical=False))

# #cpu时间统计
# print(psutil.cpu_times())

# #再实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# # for x in range(10):
# #     print(psutil.cpu_percent(interval=1,percpu=10))

# #物理x虚拟内存
# print(psutil.virtual_memory())
# #交换分区
# print(psutil.swap_memory())


# #磁盘分区
# print( psutil.disk_partitions())
# #磁盘使用情况
# print(psutil.disk_usage('/'))
# #磁盘IO
# print(psutil.disk_io_counters())

# # 获取网络读写字节／包的个数
# print(psutil.net_io_counters() )
# # 获取网络接口信息
# print(psutil.net_if_addrs())

# #获取网络接口状态
# print(psutil.net_if_stats())

#获取当前网络连接信息
# print(psutil.net_connections())



# 所有进程ID
print(psutil.pids() )

# p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
# p.name() # 进程名称

# p.exe() # 进程exe路径

# p.cwd() # 进程工作目录

# p.cmdline() # 进程启动的命令行

# p.ppid() # 父进程ID

# p.parent() # 父进程

# p.children() # 子进程列表

# p.status() # 进程状态

# p.username() # 进程用户名

# p.create_time() # 进程创建时间

# p.terminal() # 进程终端

# p.cpu_times() # 进程使用的CPU时间

# p.memory_info() # 进程使用的内存

# p.open_files() # 进程打开的文件

# p.connections() # 进程相关网络连接

# p.num_threads() # 进程的线程数量

# p.threads() # 所有线程信息

# p.environ() # 进程环境变量

# # p.terminate() # 结束进程

#模拟出ps命令的
psutil.test()
