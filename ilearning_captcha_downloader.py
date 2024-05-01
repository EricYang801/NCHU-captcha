import requests
from datetime import datetime
import os 
import time

def download_captcha():
    url = 'https://lms2020.nchu.edu.tw/sys/libs/class/capcha/secimg.php'
    params = {
        'charLens': '6',
        'codeType': 'num'
    }

    headers = {
        
        'Referer': 'https://lms2020.nchu.edu.tw/index/login?next=%2Fdashboard',
        'Accept': 'image/webp,image/avif,image/jxl,image/heic,image/heic-sequence,video/*;q=0.8,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh-Hant;q=0.9'
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        # Check if the 'images' directory exists, if not, create it
        directory = './ilearning_images/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Generate a unique filename with a timestamp
        filename = 'captcha_{}.jpg'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))
        filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print("圖片下載成功")
    else:
        print("圖片下載失敗，錯誤碼:", response.status_code)



while True:
    download_captcha()
    time.sleep(0.1)
