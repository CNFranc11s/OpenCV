import cv2
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')

filename = path_in
gry = cv2.imread(filename, 0)
# -1	無変換
# 0	グレー
# 1	カラー
# 2	任意の深度
# 3	任意のカラー
cv2.imwrite(path_out, gry)
