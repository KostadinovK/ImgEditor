# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:09:20 2018

@author: Kostadin Kostadinov
"""

import numpy as np
import cv2

def dummy(v):
    pass

cv2.namedWindow("ImgEditor v1.0")
cv2.createTrackbar("Contrast","ImgEditor v1.0",1,100,dummy)
cv2.createTrackbar("Brightness", "ImgEditor v1.0", 50, 100, dummy)
cv2.createTrackbar("Filter", "ImgEditor v1.0", 0, 1, dummy)
cv2.createTrackbar("Grayscale","ImgEditor v1.0",0,1, dummy)

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == ord('Q'):
        break

cv2.destroyAllWindows()