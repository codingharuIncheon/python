from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 프로그램을 잠깐 멈추게 하기위한 라이브러리
import time
# url로 이미지를 다운받기 위한 라이브러리
import urllib.request
 






 
#driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
driver = webdriver.ChromeOptions()
driver.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe") 


driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%ED%83%80%EC%B9%B4%ED%95%98%EC%8B%9C%20%EC%A5%AC%EB%A6%AC" )
time.sleep(3)
 
images = driver.find_elements_by_css_selector("#imgList > div > a > img")
img_url = []
 
for image in images :
    url = image.get_attribute('src')
    img_url.append(url)
 
    print(img_url)
 
 
import os 
 
img_folder = './img'
 
if not os.path.isdir(img_folder) : # 없으면 새로 생성하는 조건문 
    os.mkdir(img_folder)
    
for index, link in enumerate(img_url) :
#     start = link.rfind('.')
#     end = link.rfind('&')
#     filetype = link[start:end]
	urlretrieve(link, f'./img/{index}.jpg')