# Chapter 8 Contours and Shape Detection
import cv2
import numpy as np
# Function
def getContours(img):
    contours,hierachy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)
            perimeter=cv2.arcLength(cnt,True)
            #print(perimeter)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
            #print(len(approx))
            objcor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
            
            if objcor==3: objecttype="Tri"   
            else:
                objecttype="None"
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(imgcontour,objecttype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)

img=cv2.imread(r"C:\Users\prath\Downloads\geometry.jpg")
imgcontour=img.copy()
# Step 1 Covert BGR to Grey
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggrey,(7,7),1)
# Step 2 Canny Edge Detector
imgcanny=cv2.Canny(imgblur,50,50) 
getContours(imgcanny)




#cv2.imshow("Output",img)
#cv2.imshow("Grey",imggrey)
#cv2.imshow("Blur",imgblur)
#cv2.imshow("Canny",imgcanny)
cv2.imshow("Image Contour",imgcontour)
cv2.waitKey(0)