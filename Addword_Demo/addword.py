import cv2,os
#以下是putText()方法的官方文档说明

"""
putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) -> img
.   @brief Draws a text string.
.   
.   The function cv::putText renders the specified text string in the image. Symbols that cannot be rendered
.   using the specified font are replaced by question marks. See #getTextSize for a text rendering code
.   example.
.   
.   @param img Image.
.   @param text Text string to be drawn.
.   @param org Bottom-left corner of the text string in the image.
.   @param fontFace Font type, see #HersheyFonts.
.   @param fontScale Font scale factor that is multiplied by the font-specific base size.
.   @param color Text color.
.   @param thickness Thickness of the lines used to draw a text.
.   @param lineType Line type. See #LineTypes
.   @param bottomLeftOrigin When true, the image data origin is at the bottom-left corner. Otherwise,
.   it is at the top-left corner.
"""

current_path = os.path.abspath(__file__)
path =  os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
path_in = os.path.join(path,'lena.jpg')
path_out = os.path.join(path,'output.jpg')

#读取待插入文字的图片
img = cv2.imread(path_in)

#待插入的文字
text = "beautiful woman"  

# 图片 添加的文字 位置(width,height) 字体 字体大小 字体颜色 字体粗细
cv2.putText(img, text, (40, 500), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,255), 2)

cv2.imwrite(path_out, img)