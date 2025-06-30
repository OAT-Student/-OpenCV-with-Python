import cv2

img = cv2.imread('pythonLogo.png')

#line
#cv2.line(img,(0,0),(100,100),(255,0,0),6)

#circle
#cv2.circle(img,(100,100),75,(255,0,0),5)

#rectangle
#cv2.rectangle(img,(20,20),(100,100),(255,0,0),-1)

cv2.putText(img,'Hay !!',(100,150),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
cv2.imshow ('image',img)
cv2.waitKey(0)
cv2.destoryAllWindow()