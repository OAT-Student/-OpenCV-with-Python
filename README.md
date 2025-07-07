# OpenCV-with-Python

ใช้กับ image Processing , Computer vision

#// ติ้งตั้ง opencv

sudo apt update
sudo apt install python3-opencv

# import cv2

python3

เมื่อพิมไปแล้วจะขึ้นเป็นแบบนี้ >> ให้ใส่ว่า 

import cv2

ใช้คำสัง exit() เพื่อออก

***** ทำไม run แบบใช้ commard Line ถึงมีปัญหา แต่run แบบ start debugging ถึงได้


# ลักษณะการเก็บภาพของ opencv ใน python

จากการใช้คำสั่ง 

img = cv2.imread('pythonLogo.png')

print(img) จะได้

[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]

 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]

 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]

 ...

 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]

 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]

 [[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  [255 255 255]
  [255 255 255]
  [255 255 255]]]

  แสดงว่ามีการเก็บข้อมูลแบบ array โดย opencv จะเก็ยสีแบบ  BGR ไม่ใช่ RGB


  # การ crop รูป 
  
  จะใช้ เทคนิคเรียกว่า ROI => Region  of Interest

img_crop = img[0:167,65:245] #0:167 = row ,65:245 = column  

cv2.imshow('test',img_crop) # test' = ชื่อจากหน้าต่างที่จะเปิดขึ้นมา ,img_crop = ภาพที่จะนำมาแสดง

cv2.imwrite('cropped.png',img_crop) #'cropped.png' =ชื่อไฟล์ที่ต้องการsave ,img_crop = ไฟล์ที่จะsave




# Drawing on Image

วาดเส้นตรง(Line)

cv2.line(img,(0,0),(100,100),(255,0,0),6)
  **cv2.line ต้องอยู่ก่อน cv2.show 

  img = รูปที่ต้องการ
  (0,0) = ตำแหน่งเริ่มต้น
  (100,100) = ตำแหน่งสุดท้าย
  (255,0,0) = ค่าสี ***BGR นะ ไม่ใช่ RGB
  6 = ความหนา (thickness)

วาดวงกลม (Circle)

cv2.circle(img,(100,100),75,(255,0,0),5)
  **cv2.circle ต้องอยู่ก่อน cv2.show 

  img = รูปที่ต้องการ
  (100,100) = จุดศูนย์กลางวงกลม
  75 = รัศมี
  (255,0,0) = ค่าสี ***BGR นะ ไม่ใช่ RGB
  5 = ความหนา (thickness)
  *ถ้าอยากได้วงกลมทีบ ให้ใส่  thickness = -1


วาดสี่เหลี่ยม (rectangle)

cv2.rectangle(img,(20,20),(100,100),(255,0,0),5)
**cv2.rectangle ต้องอยู่ก่อน cv2.show 

  img = รูปที่ต้องการ
  (20,20) = จุดเริ่มต้น
  (100,100) = จุดสุดท้าย
  (255,0,0) = ค่าสี ***BGR นะ ไม่ใช่ RGB
  5 = ความหนา (thickness)
  *ถ้าอยากได้วงกลมทีบ ให้ใส่  thickness = -1

เขียนคำบรรยาย 

cv2.putText(img,'Hay !!',(100,150),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),5)

  img = รูปที่ต้องการ
  'Hay !!' = คำไม่ต้องการแสดง
  (100,150) = ตำแหน่ง
  cv2.FONT_HERSHEY_PLAIN = Fontที่ต้องการใส่
  2 = ขนาดFont
  (255,0,0) = ค่าสี ***BGR นะ ไม่ใช่ RGB
  5 = ความหนา (thickness)


# Template Matching (ตรวจจับเหรียญในภาพ) อยู่ใน 4.py
หลักการคือ แบ่งภาพ Original เป็นส่วนๆ แล้วเอาภาพ Template ไปเทียบ

การคำนวน อยู่ในไฟล์ compare_photo.png (มีหลายMode ให้เลือกใช้)

template = cv2.imread('1baht.jpg') 
  ภาพที่ต้องการเปรียบเทียบ


h, w, _ = template.shape

เก็บตัวแปร high width
ถ้า template.shape คือ (300, 400, 3):
h = 300
w = 400
3 ถูกเก็บใน _ เพราะคุณ ไม่ต้องการใช้มัน



res = cv2.matchTemplate(img, template,cv2.TMCCOEFF_NORMED)

res ย่อมาจาก resource
img = ภาพ original 
template = ภาพที่ต้องการเปรียบเทียบ
cv2.TMCCOEFF_NORMED = วิธีที่ใช้ เลือกได้จาก compare_photo.png(มีหลายMode ให้เลือกใช้)




min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

  ฟังชั่น minMaxLoc ดึงว่า จากres แล้วassign ให้คนอื่น


top_left = max_loc 
bottom_right = (top_left[0]+ w, top_left[1] + h)

  asignค่า แล้วนำไปใช้ตีกรอบ


cv2.rectangle(img, top_left,bottom_right,(0,255,255),3)
  วาดรูปสี่เหลี่ยมปกติ


# Detect object with Contour (ตรวจจับวัตถุด้วย Contour)
    web รวบรวมเกี่ยวกับ image processing 
    pyimagesearch.com

  
  ติดตั้ง Library นี้เพิ่ม
sudo apt install imutils


//ทำPre processing (แปลงรูปเป็นขาดำ  ใส่เบลอ )

gray = cv2.cvtColar(image,cv2.COLOR_BGR2GRAY)
  gray ตัวแปรที่แปลงเป็นสีเทา ขาวดำ

blurred = cv2.GaussianBlur(gray,(5,5),0)
  ใส่ฟิวเตอร์เบลอให้รูป
  gray = ภาพต้นฉบับ
  (5,5) = ขนาดของ kernel (หน้าต่าง) ที่ใช้ในการเบลอ (5, 5) หมายถึงใช้หน้าต่างขนาด 5x5 พิกเซล **ต้องเป็นเลขคี่เท่านั้น
  0 = เบี่ยงเบนมาตรฐาน 

thresh = cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1]
blurred = ภาพอินพุตที่เป็น Grayscale (และถูกเบลอแล้ว)
60 = ถ้าพิกเซลมีค่ามากกว่า 60 → จะถูกทำให้เป็นสีขาว (255)
255 = ค่าสีที่จะใช้ถ้าผ่าน threshold → ในที่นี้คือ 255 (สีขาว)
cv2.THRESH_BINARY
คือประเภทของ threshold:
ถ้าค่า > 60 → set เป็น 255
ถ้า ≤ 60 → set เป็น 0


// Contours หาว่าวัตุอยู่บริเวณไหน
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) # เก็บในlist

thresh.copy() = สร้างไฟล์ใหม่เหมือนthresh 
cv2.RETR_EXTERNAL = mode ในการหาcontours
cv2.CHAIN_APPROX_SIMPLE =  mode ในการหาcontours
imutils จะแปลงว่าของ cnts ให้user นำไปใช้งานได้ง่าย


for c in cnts:
    cv2.drawContours(image,[c],-1,(0,0,255),2)

print contourที่ได้ ทับลงimage 

# Detect Lines and Corners

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #เก็บในรูปของ int
gray = np.float32(gray) #แปลงint เป็น Float โดยใช้np มาช่วย

corners = cv2.goodFeaturesToTrack(gray,100,0.01,10) 
#detect หาจุดหามุมของภาพ 
100 = max location (เลือกจุดไม่เกิน 100 มุม)
0.01 = ความ sensitive 
10 = min distance ยิ่งค่ามากจะทำให้มีจุดน้อยลง

corners = np.int0(corners) # แปลงเป็น int กลับคืน เพื่อนำไปใช้ต่อ

for corner in corners:
    x ,y = corners.ravel() # assignค้าx y 
    cv2.circle(img,(x,y),3,(255,0,0),-1) # plot จุดจากค่าX y ข้างบน



// line detection 

canny = cv2.Canny(img, 100,200)
100 = threshold1 แต่ละภาพไม่เหมือนกัน ต้องลองปรับดู
200 = threshold2 แต่ละภาพไม่เหมือนกัน ต้องลองปรับดู

# Face Detection (Haar Cascade) การตรวจจับภาพใบหน้า

// Haar Cascade สามารถ Identity Location & identify object  สามารถ detectสิ้งที่คล้ายคลีงกันได้
// ต้องมีmodel ให้มันใช้ 
แหล่งรวมโมเดล : https://github.com/opencv/opencv 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #ใส่โมเดลที่ได้มา

gray = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)  # แปลงค่าเป็น gray 
faces = face_cascade.detectMultiScale(gray) # face_cascade = model หนึ่งตัว ,  predic detectMultiScale(gray)


for (x , y, w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) #สั่งตีกรอบวัตถุ


//ถ้าอยากสร้าง haar cascade ด้วยตัวเอง

https://patorn-j.medium.com/%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-haar-cascade-%E0%B9%84%E0%B8%A7%E0%B9%89%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%A7%E0%B8%B1%E0%B8%95%E0%B8%96%E0%B8%B8-%E0%B8%89%E0%B8%9A%E0%B8%B1%E0%B8%9A%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%A1%E0%B8%B2%E0%B8%81-%E0%B8%81-%E0%B9%84%E0%B8%81%E0%B9%88-%E0%B8%A5%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%95%E0%B8%B1%E0%B8%A7-6a2e073a7571
