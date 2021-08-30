from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import json
driver=webdriver.Chrome()
with open('cookieTest2.txt','r', newline='')as tmp:
    cookies = json.load(tmp)
driver.get("https://www.tokopedia.com/")
for curcookie in cookies:
    print(curcookie)
    driver.add_cookie(curcookie)
driver.refresh()
#go to messaging
#while check 
#if there is indicator do reply
#sleep n time