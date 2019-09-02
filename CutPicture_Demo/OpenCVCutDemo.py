import cv2
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')

img = cv2.imread(path_in)
shape = img.shape  #height，width，通道数的元组

cuted = img[0 + int(shape[0] / 4):512 - int(shape[0] / 4), 0 +
            int(shape[1] / 4):512 - int(shape[1] / 4)]
#[0:height,0:width]按坐标裁剪图片
# 取长宽的1/4，实现图片的缩放
cv2.imwrite(path_out, cuted)
