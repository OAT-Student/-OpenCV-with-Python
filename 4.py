import cv2
img = cv2.imread('Original_photo.jpg')
template = cv2.imread('1baht.jpg')

h, w, _ = template.shape

res = cv2.matchTemplate(img, template,cv2.TM_CCORR)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0]+ w, top_left[1] + h)

cv2.rectangle(img, top_left,bottom_right,(0,255,255),3)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destoryAllWindow()

# ไม่เหมือนตามที่สอน ตรวจยังได้ระดับหนึ่ง