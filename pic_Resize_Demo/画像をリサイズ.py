import cv2
import numpy as np
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')

filename = path_in
img = cv2.imread(filename, 1)
width, height = 60, 60
img = cv2.resize(img, (width, height))

cv2.imwrite(path_out, img)
