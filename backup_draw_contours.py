import numpy as np
from matplotlib import pyplot as plt
import cv2
im = cv2.imread('test_3.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print len(contours) , " , ", len(contours[0])
im_copy = np.full((1000, 1000), 1) 
print len(im_copy) , " ,", len(im_copy[0])
#cv2.drawContours(im_copy, contours, -1, (0,0,0),1,0)
#plt.imshow(im_copy)
#plt.show()

im_copy = np.zeros((1000, 1000))
cv2.fillPoly(im_copy, contours, (255,255,255))
cv2.imshow(" ", im_copy)
cv2.waitKey(5000)

for i in range(20, 20):
 cnt = contours[i*10]
 im_copy = cv2.imread('plain_paper.jpg')
 cv2.drawContours(im_copy, [cnt], -1, (0,255,0), 1, 0)
 plt.imshow(im_copy)
 plt.show()
 print i*10
