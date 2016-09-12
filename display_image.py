import numpy as np
from matplotlib import pyplot as plt
import cv2
img = cv2.imread('test.jpg')
cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
