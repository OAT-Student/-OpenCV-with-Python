import cv2
img = cv2.imread('test_face.jpg')

#Haar Cascade
#Identity Location & identify object

#start Code here
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)

for (x , y, w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)


cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destoryAllWindow()