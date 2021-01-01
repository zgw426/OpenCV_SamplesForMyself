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

outputVideo= "editV06.mp4"
mappingImg = "test-mapping.png"


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

im_src = cv2.imread( mappingImg ) # マッピングする画像

while cap.isOpened():
    ret, frame = cap.read()
    # Check if frame is not empty
    if frame is None :
        break
 
    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    frame = aruco.drawDetectedMarkers(frame, corners, ids)
    
    if np.all(ids != None):
        # 検出したARマーカーの数ループする
        for c in corners :
            x1 = (c[0][0][0], c[0][0][1]) 
            x2 = (c[0][1][0], c[0][1][1]) 
            x3 = (c[0][2][0], c[0][2][1]) 
            x4 = (c[0][3][0], c[0][3][1])   
 
            size = im_src.shape
            pts_dst = np.array([x1, x2, x3, x4])
            pts_src = np.array(
                           [
                            [0,0],
                            [size[1] - 1, 0],
                            [size[1] - 1, size[0] -1],
                            [0, size[0] - 1 ]
                           ],dtype=float
                        )
            h, status = cv2.findHomography(pts_src, pts_dst)
            temp = cv2.warpPerspective(im_src.copy(), h, (frame.shape[1], frame.shape[0])) 
            cv2.fillConvexPoly(frame, pts_dst.astype(int), 0, 16)
            frame = cv2.add(frame , temp)
            aruco.drawDetectedMarkers(frame, corners, ids, (255,0,0)) #検出したマーカに,マッピング用の画像を描画する

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
