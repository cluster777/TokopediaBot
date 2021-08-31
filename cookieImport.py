from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import json
import time
driver=webdriver.Chrome()
with open('cookieTest2.txt','r', newline='')as tmp:
    cookies = json.load(tmp)
driver.get("https://www.tokopedia.com/")
for curcookie in cookies:
    print(curcookie)
    driver.add_cookie(curcookie)
driver.refresh()
#go to messaging
time.sleep(5)
try:
    driver.find_element_by_xpath("//button[@aria-label='Tutup tampilan modal']").click()
except:
    print("nothing wrong")
driver.find_element_by_xpath("//div[@data-testid='btnHeaderInbox']").click()
driver.find_element_by_xpath("//a[@href='/chat']").click()
#while check 
#if there is indicator do reply
#sleep n time