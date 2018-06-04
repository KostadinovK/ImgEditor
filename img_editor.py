# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:09:20 2018

@author: Kostadin Kostadinov
"""

import numpy as np
import cv2
"""from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)"""

def dummy(v):
    pass
image_original = cv2.imread("test.jpeg")
image_copy = image_original.copy()
cv2.namedWindow("ImgEditor v1.0")
cv2.createTrackbar("Contrast","ImgEditor v1.0",1,200,dummy)
cv2.createTrackbar("Brightness", "ImgEditor v1.0", 100, 200, dummy)
cv2.createTrackbar("Filter", "ImgEditor v1.0", 0, 1, dummy)
cv2.createTrackbar("Grayscale","ImgEditor v1.0",0,1, dummy)

while True:
    cv2.imshow("ImgEditor v1.0",image_copy)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == ord('Q'):
        break
    contrast = cv2.getTrackbarPos("Contrast","ImgEditor v1.0")
    brightness = cv2.getTrackbarPos("Brightness","ImgEditor v1.0")
    image_copy = cv2.addWeighted(image_original,contrast,image_original,0,brightness-100)
    
    
        
cv2.destroyAllWindows()