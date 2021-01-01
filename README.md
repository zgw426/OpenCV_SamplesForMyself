## OpenCV_SamplesForMyself

OpenCVのARマーカーのライブラリArUcoのPython3サンプルスクリプト

## 概要

|ファイル名|検出対象|描画|出力|
|---|---|---|---|
|opcv_outputARmark01.py|－|ARマーカー|画像|
|opcv_outputARmark02.py|－|ARマーカー|画像|
|opcvCapImg01_drawID_outImg.py|画像|ID|画像|
|opcvCapImg02_drawText_outImg.py|画像|文字|画像|
|opcvCapImg03_drawLine_outImg.py|画像|線|画像|
|opcvCapImg04_drawRectangle_outImg.py|画像|四角形|画像|
|opcvCapImg05_drawCircle_outImg.py|画像|円|画像|
|opcvCapImg06_drawPolylines_outImg.py|画像|多角形|画像|
|opcvCapImg07_drawIMG_outImg.py|画像|画像|画像|
|opcvCapImg08_drawAxis_outImg.py|画像|3D軸|画像|
|opcvCapVideo01_drawID.py|動画|ID|－|
|opcvCapVideo02_drawID_outMP4.py|動画|ID|動画|
|opcvCapVideo03_drawRectangle_outMP4.py|動画|四角形|動画|
|opcvCapVideo04_drawText_outMP4.py|動画|文字|動画|
|opcvCapVideo05_drawAxis_outMP4.py|動画|3D軸|動画|
|opcvCapVideo06_drawImg_outMP4.py|動画|画像|動画|
|opcvCapVideo07_drawVideo_outMP4.py|動画|動画|動画|
|(dummy)test-mapping.mp4____.txt|－|－|－|
|(dummy)test-video.mp4____.txt|－|－|－|


- カラム説明
    - 検出対象
        - ARマーカーを検出する対象
        - (画像, 動画)
    - 描画
        - 検出したARマーカーに付与する情報の種類
        - (ID, 文字, 画像, 動画 など)
    - 出力
        - 実行結果をファイル出力する形式
        - (画像, 動画)
- ダミーファイル
    - mp4ファイルの変わりにダミーのテキストファイルを格納している
    - (dummy)test-mapping.mp4____.txt
        - `test-mapping.mp4`のダミーファイル
        - https://youtu.be/S-h031SBLaQ
    - (dummy)test-video.mp4____.txt
        - `test-video.mp4`のダミーファイル
        - https://youtu.be/qlqU_y5hu0k
- 画像ファイル
    - ARマーカー検出用の画像
        - test-img01.png
        - test-img02.png
        - test-img03.png
    - マッピング用の画像
        - test-mapping.png


