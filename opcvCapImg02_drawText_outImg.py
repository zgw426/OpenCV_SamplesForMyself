#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np

targetImg  = "test-img02.png"

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
outputImg  = "edit02-" + targetImg[0:-4]+".png"

def arReader( argTargetImg , argOutputImg ):

    img = cv2.imread( argTargetImg )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出

    # draw ID
    aruco.drawDetectedMarkers(img, corners, ids, (0,255,0)) #検出したマーカに描画する

    for i, corner in enumerate( corners ):
        points = corner[0].astype(np.int32)
        # マーカーの輪郭
        cv2.polylines(img, [points], True, (255,0,0))

        cv2.putText(img, str(points[0]), tuple(points[0]), cv2.FONT_HERSHEY_PLAIN, 1,(100,0,100), 2)
        cv2.putText(img, str(points[1]), tuple(points[1]), cv2.FONT_HERSHEY_PLAIN, 1,(0,255,0), 2)
        cv2.putText(img, str(points[2]), tuple(points[2]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,255), 2)
        cv2.putText(img, str(points[3]), tuple(points[3]), cv2.FONT_HERSHEY_PLAIN, 1,(255,0,0), 2)
        # テキスト描画
        # arg1 : cv.imread で開いた画像
        # arg2 : 文字列
        # arg3 : 文字列の位置(文字列の左下)
        # arg4 : フォントスタイル CV_FONT_HERSHEY_PLAIN, CV_FONT_HERSHEY_SCRIPT_SIMPLEX など
        # arg5 : フォントサイズ
        # arg6 : フォントの色
        # arg7 : フォントの太さ
        # arg8 : lineType 4, 8, cv.LINE_AA の3択

    img = Image.fromarray(img)
    img.save( argOutputImg )

arReader( targetImg , outputImg )
