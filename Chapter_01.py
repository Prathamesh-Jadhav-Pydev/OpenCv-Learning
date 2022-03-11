# First tutorial of Opencv 
# First we import opencv 
# Chapter 01 reading image,video and webcam
import cv2
import numpy as np

print("Done")
kernel=np.ones((5,5),np.uint8)
#1.reading  the image 
img=cv2.imread(r"C:\Users\prath\Downloads\train\Image_000000.jpg") #read the image
cv2.imshow("Output",img) #display the image
cv2.waitKey(0) # add delay 

#2. Video capture object 
video=cv2.VideoCapture("") #define the path 
#video is sequence of images to show capture video we use while loop below.
while True:
    success,img=video.read()
    cv2.imshow("Video Output",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
#code for video and webcam are almost same.
#3. Webcam 
webcam=cv2.VideoCapture(0)
webcam.set(3,640) #width
webcam.set(4,480) #height
webcam.set(10,100) #brightness
while True:
    success,img=webcam.read()
    cv2.imshow("Video Output",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break





