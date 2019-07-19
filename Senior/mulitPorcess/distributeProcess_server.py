#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   distributeProcess.py
@Time    :   2019/06/24 14:44:20
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 
@Desc    :   None
'''

# # here put the import lib
# import random ,time,queue

# from multiprocessing.managers import BaseManager

# from multiprocessing import freeze_support

# #发送任务队列
# task_queue=queue.Queue(10)

# #接收结果队列
# result_queue=queue.Queue(10)

# #从Basemanager继承Queuemanager
# class QueueManager(BaseManager):
#     pass
# #WIN下不能自动序列化lambda表达式下，需要先定义成函数
# def gettask():
#     return task_queue
# def getresult():
#     return result_queue

# def win_run():
#     #把Queue注册到网络上，callable参数关联Queue对象
#     QueueManager.register('get_task_queue',callable=task_queue)
#     QueueManager.register('get_result_queue',callable=result_queue)

#     # 绑定端口5000，设置验证码'abc'
#     # manager=QueueManager(address=('',5000),authkey=b'abc')
#     manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')

#     # 启动queue
#     manager.start()

#     #活的通过完了过访问的Queue对象
#     task=manager.get_task_queue()

#     result=manager.get_result_queue()

#     #将任务放入task

#     for i in range(10):
#         n=random.randint(0,10000)
#         print('Put task %d..' % n)
#         task.put(n)

#     #从result队列读取结果
#     print ('Try get results ...')

#     for i in range(10):
#         r=result.get(timeout=10)
#         print('Result: /%s ' % r)

#     #关闭
#     manager.shutdown()
#     print('master exit')
    
# if __name__ == '__main__':
#     # windows多进程可能有问题 加以下代码缓解
#     freeze_support()
#     win_run()



import time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number = 10;
#定义收发队列
task_queue = queue.Queue(task_number);
result_queue = queue.Queue(task_number);
def gettask():
    return task_queue;
def getresult():
     return result_queue;
def test():
    #windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    BaseManager.register('get_task',callable = gettask);
    BaseManager.register('get_result',callable = getresult);
    #绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地
    manager = BaseManager(address = ('127.0.0.1',5002),authkey = b'123');
    #启动
    manager.start();
    try:
        #通过网络获取任务队列和结果队列
        task = manager.get_task();
        result = manager.get_result();
        #添加任务
        for i in range(task_number):
            print('Put task %d...' % i)
            task.put(i);
        #每秒检测一次是否所有任务都被执行完
        while not result.full():
            time.sleep(1);
        for i in range(result.qsize()):
            ans = result.get();
            print('task %d is finish , runtime:%d s' % ans);
    
    except:
        print('Manager error');
    finally:
        #一定要关闭，否则会爆管道未关闭的错误
        manager.shutdown();
        
if __name__ == '__main__':
    #windows下多进程可能会炸，添加这句可以缓解
    freeze_support()
    test();