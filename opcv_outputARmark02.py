#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

# ArUcoのライブラリを導入
aruco = cv2.aruco

# 4x4のマーカー，ID番号は50までの辞書を使う
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

def main():
    # 10枚のマーカーを作るために10回繰り返す
    for i in range(10):
        ar_image = aruco.drawMarker(dictionary, i, 150) # i: ID番号，150x150ピクセル．
        fileName = "ar" + str(i).zfill(2) + ".png"  # ファイル名を "ar0x.png" の様に作る
        cv2.imwrite(fileName, ar_image) # マーカー画像を保存する

if __name__ == "__main__":
    main()
