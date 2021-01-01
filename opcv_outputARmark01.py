#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ↓ $ pip install opencv-contrib-python
import cv2

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

def arGenerator():
    fileName = "ar.png"
    generator = aruco.drawMarker(dictionary, 0, 150) # 0: ID番号，150x150ピクセル
    cv2.imwrite(fileName, generator)

    img = cv2.imread(fileName)

arGenerator()
