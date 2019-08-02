#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DemoCopyFile.py
@Time    :   2019/07/30 21:57:20
@Author  :   王翔 
@Version :   1.0
@Contact :   muumuu123@126.com
@License :   (C)Copyright 2018-2019, 王翔
@Desc    :   None
'''

# here put the import lib
'''
1.创建文件夹
2、获取old文件夹中得所有文件名字
3.使用多个进程得方式复制文件到新得文件目录

'''
import os 
from multiprocessing import Pool

def copyFiles(oldFoldenName,newFoldenName,fileName):
    "copy文件"
    fw=open(os.path.join(newFoldenName,fileName),"w")
    with open(os.path.join(oldFoldenName,fileName),"r") as f:
        fw.write(f.read(1024))

    
def main():
    oldFoldrenName=input('请输入文件夹名字')
    newFoldrenName=oldFoldrenName+"_copy"
    # os.mkdir()

    fileNames=os.lis(oldFoldrenName)
    print (fileNames)
    pool=Pool(5)
    for x in fileNames:

        pool.apply_async(copyFiles,(x,newFoldrenName,oldFoldrenName))
    pool.close()
    pool.join()
    print ('mission complete')
if __name__ == "__main__":
    main()

