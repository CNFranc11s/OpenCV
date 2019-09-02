import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

current_path = os.path.abspath(__file__)
path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path, 'lena.jpg')
path_out = os.path.join(path, 'output.jpg')
img = cv2.imread(path_in)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()