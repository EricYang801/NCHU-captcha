from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
from PIL import Image
from io import BytesIO

# 啟動瀏覽器
driver = webdriver.Chrome()

# 加載網頁
driver.get("https://portal.nchu.edu.tw/")

# 等待網頁加載
time.sleep(2)

# 找到包含 canvas 的元素
canvas_element = driver.find_element(By.ID, "codeShow")

# 將 canvas 元素的內容提取為 base64 圖片數據
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas_element)

# 將 base64 圖片數據轉換為圖片
image_data = base64.b64decode(canvas_base64)
image = Image.open(BytesIO(image_data))


file_path = "./portal_images/"
file_name = "canvas_image.jpg"

# 保存圖片（可選）
image.save(file_path + file_name, "png")

# 關閉瀏覽器
driver.quit()
