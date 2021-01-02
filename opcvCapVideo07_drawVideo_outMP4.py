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

#mappingVideo= 0 # カメラデバイス
#mappingVideo= "test-mapping.mp4" # 動画
#mappingVideo= "http://{IP Address}:8090/?action=stream" # MJPG-Streamer
mappingVideo= "test-mapping.mp4"

outputVideo= "editV07.mp4"

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50) # ARマーカー

cap = cv2.VideoCapture(targetVideo)

# 幅,高さ取得
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

#フレームレート(1フレームの時間単位はミリ秒)の取得
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# 保存用
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter( outputVideo, fmt, frame_rate, size)

fn = 0
map_vid = cv2.VideoCapture(mappingVideo)

while cap.isOpened():
    fn += 1
    if fn >= map_vid.get(cv2.CAP_PROP_FRAME_COUNT):
        fn = 0
    map_vid.set(cv2.CAP_PROP_POS_FRAMES, fn)
    ret_v, im_src = map_vid.read()
    # Capture frame-by-frame
    ret, frame = cap.read()
    if frame is None :
        break
    scale_percent = 100 # percent of original size
    width  = int(frame.shape[1] * scale_percent / 100) 
    height = int(frame.shape[0] * scale_percent / 100) 
    dim = (width, height) 
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA) 

    org_frame = frame
    # Check if frame is not empty
    if not ret_v:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    parameters = aruco.DetectorParameters_create()
    corners, ids, _ = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
    if np.all(ids != None):
        for c in corners :
            x1 = (c[0][0][0], c[0][0][1]) 
            x2 = (c[0][1][0], c[0][1][1]) 
            x3 = (c[0][2][0], c[0][2][1]) 
            x4 = (c[0][3][0], c[0][3][1])   
            im_dst = frame
 
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
            #project corners into frame
            temp = cv2.warpPerspective(im_src.copy(), h, (org_frame.shape[1], org_frame.shape[0])) 
            cv2.fillConvexPoly(org_frame, pts_dst.astype(int), 0, 16)
            org_frame = cv2.add(org_frame, temp)
        cv2.imshow('frame', org_frame)
        # Output as video data
        writer.write(frame)
    else:
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything:
writer.release()
cap.release()
cv2.destroyAllWindows()
