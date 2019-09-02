import cv2
import numpy as np
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')
filename = path_in
# 白黒画像で画像を読み込み
img = cv2.imread(filename, 1)

# ORB
detector = cv2.ORB_create()

# 特徴検出
keypoints = detector.detect(img)

# 画像への特徴点の書き込み
img_orb = cv2.drawKeypoints(img, keypoints, None)

cv2.imwrite(path_out, img_orb)