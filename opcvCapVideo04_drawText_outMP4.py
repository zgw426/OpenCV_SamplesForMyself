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
outputVideo = "editV04.mp4"

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

        cv2.putText(frame, str("A"), tuple(points[0]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 1)
        cv2.putText(frame, str("B"), tuple(points[1]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 1)
        cv2.putText(frame, str("C"), tuple(points[2]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 1)
        cv2.putText(frame, str("D"), tuple(points[3]), cv2.FONT_HERSHEY_PLAIN, 1,(0,0,0), 1)
        # テキスト描画
        # arg1 : cv.imread で開いた画像
        # arg2 : 文字列
        # arg3 : 文字列の位置(文字列の左下)
        # arg4 : フォントスタイル CV_FONT_HERSHEY_PLAIN, CV_FONT_HERSHEY_SCRIPT_SIMPLEX など
        # arg5 : フォントサイズ
        # arg6 : フォントの色
        # arg7 : フォントの太さ
        # arg8 : lineType 4, 8, cv.LINE_AA の3択

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
