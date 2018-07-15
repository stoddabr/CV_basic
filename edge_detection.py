import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('masked_crop.JPG', 0)
ret, thresh1 = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
#cv.imshow('image', thresh1)

edges = cv.Canny(thresh1, 10, 500)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(thresh1, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.show()

edges = thresh1
edges = cv.Canny(thresh1,10,150,apertureSize = 3)
cv.Canny
cv.imshow('image', edges)
cv.waitKey(0)
minLineLength = 10
maxLineGap = 1
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 1, minLineLength, maxLineGap)
print(lines)
for x1, y1, x2, y2 in lines[0]:
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

cv.imshow('image', img)

cv.waitKey(0)
