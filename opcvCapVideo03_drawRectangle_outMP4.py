#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
import cv2.aruco as aruco
import numpy as np

#targetVideo = 0 # カメラデバイス
#targetVideo = "test-video.mp4" # 動画
#targetVideo = "http://{IP Address}:8090/?action=stream" # MJPG-Streamer

targetVideo = "test-video.mp4"
cap = cv2.VideoCapture( targetVideo )
outputVideo = "editV03.mp4"

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

while cap.isOpened():
    ret, frame = cap.read()
    # Check if frame is not empty
    if frame is None :
        break
 
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    
    for i, corner in enumerate( corners ):
        points = corner[0].astype(np.int32)
        cv2.rectangle(frame,tuple(points[0]),tuple(points[1]),(200,  0,  0),3)
        cv2.rectangle(frame,tuple(points[1]),tuple(points[2]),(  0,200,  0),3)
        cv2.rectangle(frame,tuple(points[2]),tuple(points[3]),(  0,  0,200),3)
        cv2.rectangle(frame,tuple(points[3]),tuple(points[0]),(100,100,  0),3)

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
