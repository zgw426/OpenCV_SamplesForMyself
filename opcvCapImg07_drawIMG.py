#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
import cv2

targetImg  = "test-img02.png"
mappingImg = "test-mapping.png"

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
outputImg  = "edit07-" + targetImg[0:-4]+".png"
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50) # ARマーカー
parameters = aruco.DetectorParameters_create()

def arReader():
    img = cv2.imread( targetImg ) # ARマーカーを含む画像
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_src = cv2.imread( mappingImg ) # マッピングする画像
    im_src = cv2.cvtColor(im_src, cv2.COLOR_BGR2RGB)

    # ARマーカを検出
    ## type(ids)= <class 'numpy.ndarray'> ※ARマーカ―検出
    ## type(ids)= <class 'NoneType'>      ※ARマーカ―未検出
    ## corners: 検出した各ARマーカーの4隅の座標
    corners, ids, _ = aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    
    if np.all(ids != None):
        # 検出したARマーカーの数ループする
        for c in corners :
            x1 = (c[0][0][0], c[0][0][1]) 
            x2 = (c[0][1][0], c[0][1][1]) 
            x3 = (c[0][2][0], c[0][2][1]) 
            x4 = (c[0][3][0], c[0][3][1])   
 
            size = im_src.shape
            pts_dst = np.array([x1, x2, x3, x4])
            pts_src = np.array(
                           [
                            [0,0],
                            [size[1] - 1, 0],
                            [size[1] - 1, size[0] -1],
                            [0, size[0] - 1 ]
                           ],dtype=float
                        )
            h, status = cv2.findHomography(pts_src, pts_dst)
            temp = cv2.warpPerspective(im_src.copy(), h, (img.shape[1], img.shape[0])) 
            cv2.fillConvexPoly(img, pts_dst.astype(int), 0, 16)
            img = cv2.add(img , temp)
            aruco.drawDetectedMarkers(img, corners, ids, (255,0,0)) #検出したマーカに,マッピング用の画像を描画する
    img = Image.fromarray(img)
    img.save( outputImg )

arReader()
