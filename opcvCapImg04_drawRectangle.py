#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np

targetImg  = "test-img02.png"

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
outputImg  = "edit04-" + targetImg[0:-4]+".png"

def arReader( argTargetImg , argOutputImg ):

    img = cv2.imread( argTargetImg )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出

    for i, corner in enumerate( corners ):
        points = corner[0].astype(np.int32)
        cv2.rectangle(img,tuple(points[0]),tuple(points[1]),(200,  0,  0),3)
        cv2.rectangle(img,tuple(points[1]),tuple(points[2]),(  0,200,  0),3)
        cv2.rectangle(img,tuple(points[2]),tuple(points[3]),(  0,  0,200),3)
        cv2.rectangle(img,tuple(points[3]),tuple(points[0]),(100,100,  0),3)

    img = Image.fromarray(img)
    img.save( argOutputImg )

arReader( targetImg , outputImg )
