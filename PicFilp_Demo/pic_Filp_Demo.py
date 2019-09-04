import cv2
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')

img = cv2.imread(path_in)
flip = cv2.flip(img, 0)  #3个参数控制翻转,1:水平翻转，0：垂直翻转，-1：水平垂直翻转
cv2.imwrite(path_out, flip)