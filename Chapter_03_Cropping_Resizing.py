#Chapter 3 Cropping and resizing
import cv2
import numpy as np
# Opencv convention
# Origin of image at the top left corner 
# x-axis on right side
# y-axis on down side

# 1.Reszie the image
img=cv2.imread(r"C:\Users\prath\Downloads\mickey.jpg") #read the image
cv2.imshow("Output",img) #display the image
#check the dimension of image 
height,width,channel=img.shape
print(f"Width is {width} and Height is {height} and RGB is {channel}")

# Resize the image 
imgResize=cv2.resize(img,(500,400)) #(width,height)
cv2.imshow("Resize Image",imgResize)
height,width,channel=imgResize.shape
print(f"Width is {width} and Height is {height} and RGB is {channel}")


# Cropping the image 
imgCrop=img[0:600,200:900] # [height,width]
cv2.imshow("Crop Image",imgCrop)
cv2.waitKey(0)