# load image
# print image
# crop
# save

import cv2

img = cv2.imread('pythonLogo.png') 
img_crop = img[0:167,65:245] #0:167 = row ,65:245 = column  

cv2.imshow('test',img_crop) # test' = ชื่อจากหน้าต่างที่จะเปิดขึ้นมา ,img_crop = ภาพที่จะนำมาแสดง

cv2.imwrite('cropped.png',img_crop) #'cropped.png' =ชื่อไฟล์ที่ต้องการsave ,img_crop = ไฟล์ที่จะsave


cv2.waitKey(0)
 #เปิด window ทำงานต่อเนื่องจนกว่าจะได้รับinput จากkeyborad

cv2.destroyAllWindows() # ปิดหน้าต่างทุกอันที่เปิดอยู่

