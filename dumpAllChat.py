from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time
import scrapper
import chatbot

chrome_options = Options()
chrome_options.add_argument("--headless")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument('window-size=1920x1080');
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
with open('cookieTestmm.txt','r', newline='')as tmp:
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

driver.get("https://seller.tokopedia.com/chat") 
time.sleep(5)

    # remove pin verification notification
try:
    driver.find_element_by_xpath("//button[@aria-label='Tutup tampilan modal']").click()
except:
    print("nothing wrong")
#the check chat loop
#check for indicator and get all which have it
found=scrapper.get_allChatname(driver.page_source)
#for each chat with indicator do
res=[]  
for find in found:

    print(find)
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='{name}']".format(name=find['name'])).click()
    #now chat should be open get the content
    time.sleep(7)
    message=scrapper.get_allchat(driver.page_source)
    message_set=set(message)
    res_set=set(res)
    difference=message_set-res_set
    res=res+list(difference)
with open("./dumpChat.json", "w") as f:
    json.dump(res, f, indent = 6)
#while check 
#if there is indicator do reply
#sleep n time