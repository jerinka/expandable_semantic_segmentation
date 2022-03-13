#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import os.path as osp
import cv2
import numpy as np

# from sys import argv

def json2mask(json_file='dataset/train',outpath='dataset/dataXY/train', outHW=(256,256)):
 
    cv2.namedWindow(winname='img', flags=cv2.WINDOW_NORMAL)
    cv2.namedWindow(winname='mask', flags=cv2.WINDOW_NORMAL)

    list_path = [f for f in os.listdir(json_file) if f.endswith('.json')]
    if len(list_path):
        outpathimg=osp.join(outpath,'img')
        outpathmask=osp.join(outpath,'mask')
        os.makedirs(name=outpathimg, exist_ok=True)
        os.makedirs(name=outpathmask, exist_ok=True)
    labels = []
    for i in range(0,len(list_path)):
        path = os.path.join(json_file,list_path[i])
        if os.path.isfile(path):
            data = json.load(open(path))
        img_path = os.path.join(json_file,list_path[i].replace('.json','.jpg'))
        img = cv2.imread(img_path)
        mask  = np.zeros(img.shape[:2], dtype=np.uint8)
        
        #import pdb;pdb.set_trace()

        for j in range(len(data['shapes'])):
            points = data['shapes'][j]['points']
            label = data['shapes'][j]['label']
            if label not in labels:
                labels.append(label)
            ind = labels.index(label)
            #Draw filled polygon
            cv2.fillPoly(mask, np.array([points], dtype=np.int32),color=ind+1, lineType=cv2.LINE_8)
        img = cv2.resize(img, dsize=outHW)
        mask = cv2.resize(mask, dsize=outHW)

        cv2.imwrite(os.path.join(outpathimg,list_path[i].replace('.json','.png')),img)
        cv2.imwrite(os.path.join(outpathmask,list_path[i].replace('.json','.png')),mask)
        cv2.imshow('img', img)
        cv2.imshow('mask', mask*64)
        k=cv2.waitKey(100)
        if k==27:
            break

if __name__ == '__main__':
    #base64path = argv[1]
    json2mask(json_file='dataset/train',outpath='dataset/dataXY/train', outHW=(128,128))
    json2mask(json_file='dataset/val',outpath='dataset/dataXY/val', outHW=(128,128))