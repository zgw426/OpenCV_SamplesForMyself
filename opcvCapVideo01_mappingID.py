#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
import cv2.aruco as aruco

#targetVideo = 0 # カメラデバイス
#targetVideo = "test-video.mp4" # 動画
#targetVideo = "http://{IP Address}:8090/?action=stream" # MJPG-Streamer

targetVideo = "test-video.mp4"

cap = cv2.VideoCapture( targetVideo )

while cap.isOpened():

    # Capture frame-by-frame
    ret, frame = cap.read()
 
    scale_percent = 50 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    # Check if frame is not empty
    if not ret:
        continue

    # Set AR Marker
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything:
cap.release()
cv2.destroyAllWindows()
