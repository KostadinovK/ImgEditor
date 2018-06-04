# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:09:20 2018

@author: Kostadin Kostadinov
"""

import numpy as np
import cv2
from tkinter import filedialog
from tkinter import *

choose_window = Tk()
choose_window.withdraw()
image =  filedialog.askopenfilename(initialdir = "/",title = "Select a picture to edit",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
choose_window.destroy()


identity_kernel = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        ]) 

edge_detection = np.array([
        [-1, -1, -1],
        [-1, 8 , -1],
        [-1, -1, -1]
        ])

sharpen = np.array([
        [0, -1, 0],
        [-1, 5 , -1],
        [0, -1, 0]
        ])

box_blur = np.array([
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
        ])


kernels = [identity_kernel,edge_detection,sharpen,box_blur]

def dummy(v):
    pass
image_original = cv2.imread(image)
extension = ""
start_index = 0
for c in image:
    if c == '.':
        start_index += 1
        break
    else:
        start_index += 1
filename = image[:start_index-1]
print(filename)
extension = image[start_index-1:]
print(extension)
image_copy = image_original.copy()

gray_original = cv2.cvtColor(image_original,cv2.COLOR_BGR2GRAY)
gray_copy = gray_original.copy()

cv2.namedWindow("ImgEditor v1.0")

cv2.createTrackbar("Contrast","ImgEditor v1.0",1,200,dummy)
cv2.createTrackbar("Brightness", "ImgEditor v1.0", 100, 200, dummy)
cv2.createTrackbar("Filter", "ImgEditor v1.0", 0, len(kernels)-1, dummy)
cv2.createTrackbar("Grayscale","ImgEditor v1.0",0,1, dummy)

while True:
    is_grayscale = cv2.getTrackbarPos("Grayscale","ImgEditor v1.0")
    if is_grayscale == 0:
        cv2.imshow("ImgEditor v1.0",image_copy)
    else:
        cv2.imshow("ImgEditor v1.0",gray_copy)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == ord('Q'):
        break
    elif k == ord('s') or k == ord('S'):
        if is_grayscale == 0:
            cv2.imwrite(filename + "_output"+extension,image_copy)
        else:
            cv2.imwrite(filename + "_output"+extension,gray_copy)
        
    contrast = cv2.getTrackbarPos("Contrast","ImgEditor v1.0")
    brightness = cv2.getTrackbarPos("Brightness","ImgEditor v1.0")
    kernel = cv2.getTrackbarPos("Filter","ImgEditor v1.0")
    
    
    image_copy = cv2.filter2D(image_original,-1,kernels[kernel])
    gray_copy = cv2.filter2D(gray_original,-1,kernels[kernel])
    image_copy = cv2.addWeighted(image_copy,contrast,image_original,0,brightness-100)
    gray_copy = cv2.addWeighted(gray_copy,contrast,gray_original,0,brightness-100)
    
    if is_grayscale == 1:
        cv2.imshow("ImgEditor v1.0",gray_copy)
cv2.destroyAllWindows()