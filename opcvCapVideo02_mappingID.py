#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
import cv2.aruco as aruco

#targetVideo = 0 # カメラデバイス
#targetVideo = "test-video.mp4" # 動画
#targetVideo = "http://{IP Address}:8090/?action=stream" # MJPG-Streamer

targetVideo = "test-video.mp4"
outputVideo = "editV02-" + targetVideo[0:-4]+".mp4"

#cap = cv2.VideoCapture('test-video.mp4')
cap = cv2.VideoCapture( targetVideo )

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
