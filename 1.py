# การแสดงภาพใน opencv

import cv2

img = cv2.imread('pythonLogo.png') #ดึงภาพเข้า cv2 ไปอยู่ใน ram

cv2.imshow('test',img) # test' = ชื่อจากหน้าต่างที่จะเปิดขึ้นมา ,img = ภาพที่จะนำมาแสดง

cv2.waitKey(0)
 #เปิด window ทำงานต่อเนื่องจนกว่าจะได้รับinput จากkeyborad

cv2.destroyAllWindows() # ปิดหน้าต่างทุกอันที่เปิดอยู่


