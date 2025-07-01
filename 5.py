import cv2
import imutils

image = cv2.imread('ch5.jpg')

#Pre processing
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1]

#Contours
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) # เก็บในlist

for c in cnts:
    cv2.drawContours(image,[c],-1,(0,0,255),2)
                     
    
cv2.imshow("Image",image)

cv2.waitKey(0)
cv2.destoryAllWindow()