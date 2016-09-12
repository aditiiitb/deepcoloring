import numpy as np
from matplotlib import pyplot as plt
import cv2
import random
def random_color():
 rgbl = [255,0,0]
 random.shuffle(rgbl)
 return tuple(rgbl)

im = cv2.imread('test_3.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print len(contours) , " , ", len(contours[0])
print len(hierarchy), ", ", len(hierarchy[0]), " ,", hierarchy[0][0]
im_copy = np.zeros((1000, 1000))
for i in range(0, 300):
 cnt = contours[i]
 #im_copy = np.zeros((1000,1000))
 cv2.drawContours(im_copy, [cnt], 0, (random.randint(0, 100), random.randint(200,255), random.randint(100,200)), -1, 8)
 #plt.imshow(im_copy)
 #plt.show()
 #print i*10

plt.imshow(im_copy)
plt.show()
