# Chapter 04 Shapes and Texts
import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
#img[:]=255,0,0 #BGR Blue color display

# 1. Line
cv2.line(img,(0,0),(300,300),(0,255,0),3) #<-(img,start_point,end_point,color,thickness)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #diagonal line

# 2. Rectangle
#cv2.rectangle(img,(10,10),(100,100),(0,255,0),3) #<-(img,start_point,end_point,color,thickness)
cv2.rectangle(img,(10,10),(100,100),(0,255,0),cv2.FILLED)

# 3. Circle
#cv2.circle(img,(200,300),40,(255,0,0),4)
cv2.circle(img,(200,300),40,(255,0,0),cv2.FILLED)


# 4.Text
cv2.putText(img,"Demo text",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),4)
#cv2.putText(img,text,origin,fontface,fontscale,color,thickness,linetype,bottomLeftOrigin,)

cv2.imshow("Image",img)
cv2.waitKey(0)