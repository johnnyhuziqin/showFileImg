#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
#%matplotlib inline
from PIL import Image


def getImgSize(path):
    img = Image.open(path)
    #print("img size:%rx%d"%(img.size[0],img.size[1]))
    return img.size

import os

def IsSubString(SubStrList,Str):
    flag=False
    for substr in SubStrList:
        #print("sub:%s,%s"%(substr,Str))
        if (substr in Str):
            flag=True
            break

    return flag

def GetFileList(FindPath,FlagStr=[]):
    FileList=[]
    FileNames=os.listdir(FindPath)
    #print(FileNames)
    if (len(FileNames)>0):
       for fn in FileNames:
           if (len(FlagStr)>0):
               #返回指定类型的文件名
               if (IsSubString(FlagStr,fn)):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
           else:
               #默认直接返回所有文件名
                fullfilename=os.path.join(FindPath,fn)
                FileList.append(fullfilename)

    #对文件名排序
    if (len(FileList)>0):
        FileList.sort()

    return FileList

def  showFileImage(fileList,num_x = 2):
    num_pic = len(fileList)
    x_id = 0
    y_id = 0
    #num_x = num_x
    num_y = (num_pic+num_x-1)/num_x

    width = 10
    if num_x == 1:
        width = num_x * 30
    else:
        width = num_x * 6
        
    height = 10
    if num_x == 1:
        height = num_y*10
    else:
        height = num_y*6
        
    print(width,height)    
    fig, axs = plt.subplots(num_y, num_x,figsize=(width,height))
    #fig, axs = plt.subplots(num_y, num_x)
    #plt.suptitle('pic list',fontsize = 20)
    #plt.figure(figsize=(20,60))

#    plt.autoscale(enable=False, axis=u'x',tight=False)
#    fig.autoscale(enable=False, axis=u'x',tight=False)
    for pic_id in range(num_pic):
        if x_id >= num_x:
            x_id = 0
            y_id = y_id + 1
        if num_y>1:
            if num_x > 1:
                axs_n = axs[y_id,x_id]
            else: 
                axs_n = axs[y_id]
        else:
            if num_x > 1:
                axs_n = axs[x_id]
            else:
                axs_n = axs
        path = fileList[pic_id]
        image = plt.imread(path)
        axs_n.imshow(image)
        #axs_n.axis('off')
        fileName = os.path.split(path)[1]
        axs_n.set_title(fileName,fontsize=16)
        imgSize = getImgSize(path)
        axs_n.set_xlabel('size:{}'.format(imgSize),fontsize=16)
        x_id = x_id + 1

def showDirPics(path,num_x = 2):
    fileListInDir = GetFileList(path,['png','jpg'])
    print("total files:%d"%(len(fileListInDir)))
    showFileImage(fileListInDir,num_x)
