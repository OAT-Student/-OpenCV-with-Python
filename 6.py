import numpy as np
import cv2

img = cv2.imread('pythonLogo.png')


canny = cv2.Canny(img, 100, 200)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = corners.astype(int) 

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('test', img)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
