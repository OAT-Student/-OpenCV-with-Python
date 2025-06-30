# load image
# print image
# crop
# save

import cv2

img = cv2.imread('pythonLogo.png') 
img_crop = img[0:167,65:245] #0:167 = row ,65:245 = column  

cv2.imshow('test',img_crop) # test' = ชื่อจากหน้าต่างที่จะเปิดขึ้นมา ,img = ภาพที่จะนำมาแสดง
cv2.imshow('crop',img) # test' = ชื่อจากหน้าต่างที่จะเปิดขึ้นมา ,img = ภาพที่จะนำมาแสดง


cv2.waitKey(0)
 #เปิด window ทำงานต่อเนื่องจนกว่าจะได้รับinput จากkeyborad

cv2.destroyAllWindows() # ปิดหน้าต่างทุกอันที่เปิดอยู่

