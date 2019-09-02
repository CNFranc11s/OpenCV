import cv2
import numpy as np
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')

filename = path_in
# 白黒画像で画像を読み込み
img = cv2.imread(filename, 0)

# 画像サイズの取得(横, 縦)
size = tuple([img.shape[1], img.shape[0]])

# 画像の中心位置(x, y)
center = tuple([int(size[0] / 2), int(size[1] / 2)])

# 回転させたい角度（正の値は反時計回り）
angle = 180.0

# 拡大比率
scale = 1.0

# 回転変換行列の算出
rot_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# アフィン変換
rot_img = cv2.warpAffine(img, rot_matrix, size, flags=cv2.INTER_CUBIC)

# ORB (Oriented FAST and Rotated BRIEF)
detector = cv2.ORB_create()

# 特徴検出
kp1, des1 = detector.detectAndCompute(img, None)
kp2, des2 = detector.detectAndCompute(rot_img, None)

# マッチング処理
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# マッチング上位20個の特徴点を線でリンクして画像に書き込む
match_img = cv2.drawMatches(img,
                            kp1,
                            rot_img,
                            kp2,
                            matches[:20],
                            None,
                            flags=2)

cv2.imwrite(path_out, match_img)