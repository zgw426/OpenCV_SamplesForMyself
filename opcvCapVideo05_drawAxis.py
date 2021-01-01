#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
import cv2.aruco as aruco
import numpy as np

#targetVideo = 0 # カメラデバイス
#targetVideo = "test-video.mp4" # 動画
#targetVideo = "http://{IP Address}:8090/?action=stream" # MJPG-Streamer

targetVideo = "http://raspi102.local:8090/?action=stream" # MJPG-Streamer"

cap = cv2.VideoCapture( targetVideo )
outputVideo = "editV05-out.mp4"

# Set AR Marker
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

# 幅,高さ取得
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

#フレームレート(1フレームの時間単位はミリ秒)の取得
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# 保存用
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter( outputVideo, fmt, frame_rate, size)

parameters =  aruco.DetectorParameters_create()
# CORNER_REFINE_NONE, no refinement. CORNER_REFINE_SUBPIX, do subpixel refinement. CORNER_REFINE_CONTOUR use contour-Points
parameters.cornerRefinementMethod = aruco.CORNER_REFINE_CONTOUR

cameraMatrix = np.array( 
   [[1.42068235e+03,0.00000000e+00,9.49208512e+02],
    [0.00000000e+00,1.37416685e+03,5.39622051e+02],
    [0.00000000e+00,0.00000000e+00,1.00000000e+00]] )
distCoeffs = np.array( [1.69926613e-01,-7.40003491e-01,-7.45655262e-03,-1.79442353e-03, 2.46650225e+00] )

while cap.isOpened():
    ret, frame = cap.read()
    # Check if frame is not empty
    if frame is None :
        break
 
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame = aruco.drawDetectedMarkers(frame, corners, ids)

    rvecs, tvecs, _objPoints = aruco.estimatePoseSingleMarkers(corners, 0.05, cameraMatrix, distCoeffs)
    if ids is not None:
        for i in range( ids.size ):
            aruco.drawAxis(frame, cameraMatrix, distCoeffs, rvecs[i], tvecs[i], 0.1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # Output as video data
    writer.write(frame)

    if not ret:
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything:
writer.release()
cap.release()
cv2.destroyAllWindows()
