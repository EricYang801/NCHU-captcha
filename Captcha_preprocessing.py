import cv2

# 讀取圖像
img = cv2.imread('captcha.png')

# 將影像轉換為灰度
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
_, binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 顯示二值化影像
cv2.imshow('Binary Image', binary_img)

# 定義形態學操作的核心
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 侵蝕
eroded_img = cv2.erode(binary_img, kernel)
cv2.imshow('Eroded Image', eroded_img)

# 膨脹
dilated_img = cv2.dilate(eroded_img, kernel)
cv2.imshow('Dilated Image', dilated_img)

# 等待按鍵，然後關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()