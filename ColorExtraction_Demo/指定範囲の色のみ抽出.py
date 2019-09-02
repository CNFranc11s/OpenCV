import cv2
import numpy as np
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')

filename = path_in
img = cv2.imread(filename, 1)
# 将输入图像从一个色彩空间转换到另一个色彩空间。
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 设置颜色范围
lower_color = np.array([20, 50, 50])
upper_color = np.array([255, 255, 255])

img_mask = cv2.inRange(hsv, lower_color, upper_color)

img_color = cv2.bitwise_and(img, img, mask=img_mask)

cv2.imwrite(path_out, img_color)
