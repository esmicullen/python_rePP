from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
# 추후 업데이트 용 임포트들
import os
from PIL.Image import Image
from PIL import Image
import random

key = input('검색어 입력 >>')

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

elem = driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf >  form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")

elem.send_keys(key)
elem.send_keys(Keys.RETURN)
elem = driver.find_element(By.TAG_NAME, "body")

for i in range(50):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try:
    driver.find_element(By.CSS_SELECTOR, '#islmp > div > div > div > div > div.gBPM8 >div.qvfT1 > div.YstHxe > input')

    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
except:
    pass

links = []

images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")

for image in images:
    # 이미지 소스 주소가 있다면 진행
    if image.get_attribute('src') is not None:
        # 이미지 다운로드 링크 주소를 리스트에 추가
        links.append(image.get_attribute('src'))

print("찾은 이미지 개수 : ", len(links))

for i, k in enumerate(links):
    url = k
    urllib.request.urlretrieve(url, "D:\\joshua\\img" + str(i) + ".jpg")

print("다운로드 완료")

# initial_count = 0
# dir = "D:/joshua"
# for path in os.listdir(dir):
#     if os.path.isfile(os.path.join(dir, path)):
#         initial_count += 1
#
# su = random.randint(1,initial_count)
#
# print(su)
#
# sajin = Image.open(f'img.{su}')
#
# sajin.show()