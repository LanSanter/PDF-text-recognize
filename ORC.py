from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os
# 將PDF檔轉換成PIL圖像對象
pages = convert_from_path(r'C:\Users\Tommy\Desktop\HW\input.pdf')
num_pages = 0
# 逐頁將PIL圖像對象轉換成PNG格式的圖片檔
for i, page in enumerate(pages):
    page.save(f'page_{i+1}.png', 'PNG')
    num_pages += 1

for i in range(1,num_pages+1):
    input_path=f'page_{i}.png'
    output_path=f'page_{i}.png'
    with Image.open(input_path) as im:
        im_rotated = im.rotate(-90, expand=True)
        im_rotated.save(output_path)
    




# 設定Tesseract的執行路徑（可選）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata" -l chi_tra_vert'


# 遍歷所有PNG圖片，進行文字識別
for i in range(1, num_pages+1):
    # 讀取PNG圖片
    img = Image.open(f'page_{i}.png')

    # 進行文字識別
    text = pytesseract.image_to_string(img, lang='chi_tra_vert', config=tessdata_dir_config)
    text = text.replace(' ', '')

    # 將識別結果輸出到TXT檔
    with open('output.txt', 'a', encoding='utf-8') as f:
        f.write(f'Page {i}\n{text}\n\n')
