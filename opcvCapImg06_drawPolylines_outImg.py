#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np

targetImg  = "test-img02.png"

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
outputImg  = "edit06-" + targetImg[0:-4]+".png"

def arReader( argTargetImg , argOutputImg ):

    img = cv2.imread( argTargetImg )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出

    for i, corner in enumerate( corners ):
        points = corner[0].astype(np.int32)
        # [Open CV] cv2.polylines(多角形)
        # http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html
        pts = np.array(
            [
                tuple(points[0]),
                tuple(points[1]),
                tuple(points[2]),
                tuple(points[3]),
                tuple(points[0]),
                tuple(points[2]),
                tuple(points[3]),
                tuple(points[1]),
            ], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,255))

    img = Image.fromarray(img)
    img.save( argOutputImg )

arReader( targetImg , outputImg )
