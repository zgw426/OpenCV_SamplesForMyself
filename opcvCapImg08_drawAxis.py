#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from PIL import Image
import numpy as np

targetImg  = "test-img02.png"

aruco = cv2.aruco
outputImg  = "edit08-" + targetImg[0:-4]+".png"
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

parameters =  aruco.DetectorParameters_create()
# CORNER_REFINE_NONE, no refinement. CORNER_REFINE_SUBPIX, do subpixel refinement. CORNER_REFINE_CONTOUR use contour-Points
parameters.cornerRefinementMethod = aruco.CORNER_REFINE_CONTOUR

cameraMatrix = np.array( 
   [[1.42068235e+03,0.00000000e+00,9.49208512e+02],
    [0.00000000e+00,1.37416685e+03,5.39622051e+02],
    [0.00000000e+00,0.00000000e+00,1.00000000e+00]] )
distCoeffs = np.array( [1.69926613e-01,-7.40003491e-01,-7.45655262e-03,-1.79442353e-03, 2.46650225e+00] )

def arReader():

    img = cv2.imread( targetImg )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出
    # draw ID
    #aruco.drawDetectedMarkers(img, corners, ids, (0,255,0)) #検出したマーカに描画する
    rvecs, tvecs, _objPoints = aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs)

    if ids is not None:
        for i in range( ids.size ):
            aruco.drawAxis(img, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.1)

    img = Image.fromarray(img)
    img.save( outputImg )

arReader()
