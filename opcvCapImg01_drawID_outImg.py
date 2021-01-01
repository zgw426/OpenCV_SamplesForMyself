#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from PIL import Image

targetImg  = "test-img02.png"

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
outputImg  = "edit01-" + targetImg[0:-4]+".png"

def arReader( argTargetImg , argOutputImg ):

    img = cv2.imread( argTargetImg )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出

    # draw ID
    aruco.drawDetectedMarkers(img, corners, ids, (0,255,0)) #検出したマーカに描画する
    img = Image.fromarray(img)
    img.save( argOutputImg )

arReader( targetImg , outputImg )
