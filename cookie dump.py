from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import json
driver=webdriver.Chrome()
driver.get("https://www.tokopedia.com/")
time.sleep(100)
print(driver.get_cookies())
with open('cookieTest2.txt','w', newline='')as tmp:
    json.dump(driver.get_cookies(), tmp, indent = 6)
driver.close()