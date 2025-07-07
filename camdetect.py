import cv2
import time

# เปิดกล้อง (0 หมายถึงกล้องตัวหลักของ notebook)
cap = cv2.VideoCapture(0)

# ตั้งค่า FPS เป็น 30 (ถ้าอุปกรณ์รองรับ)
cap.set(cv2.CAP_PROP_FPS, 30)

# ตั้งความกว้าง/สูง (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # แปลงภาพเป็น grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ประมวลผล Canny edge บน grayscale
    canny = cv2.Canny(gray, 100, 200)

    # แสดงผล (ภาพ Canny เป็นขาวดำอยู่แล้ว)
    cv2.imshow('Canny Edge Detection', canny)

    # กด 'q' เพื่อออก
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดการใช้งานกล้อง
cap.release()
cv2.destroyAllWindows()
