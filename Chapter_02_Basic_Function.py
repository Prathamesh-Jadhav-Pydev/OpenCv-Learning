import cv2
import numpy as np

print("Done")
kernel=np.ones((5,5),np.uint8)
# Basic function
# 1.Gery Image
img=cv2.imread(r"C:\Users\prath\Downloads\mickey.jpg")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Grey Image
imgblur=cv2.GaussianBlur(imggray,(7,7),0) # blur image #k-size is kernel size (odd number) ,sigmax=0
imgcanny=cv2.Canny(img,150,200) # Canny image edge detection
imgDialation=cv2.dilate(imgcanny,kernel,iterations=1) #dialation image
#opp to dialation is eroded
imgeroded=cv2.erode(imgDialation,kernel,iterations=1) #eroded image

cv2.imshow("Grey Image",imggray)
cv2.imshow("Blur Image",imgblur)
cv2.imshow("Canny Image",imgcanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgeroded)
cv2.waitKey(0)