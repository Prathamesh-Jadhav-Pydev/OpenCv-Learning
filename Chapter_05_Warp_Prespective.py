# Chapter 5 Warp Prespective
import cv2
import numpy as np
img=cv2.imread(r"C:\Users\prath\Downloads\mickey.jpg") #read the image
cv2.imshow("Output",img)
width,height=250,350
pts1=np.float32([[],[],[],[]]) # get this value when you open a image in paint
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)