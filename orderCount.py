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
import Tools.scrapper as scrapper

chrome_options = Options()
chrome_options.add_argument("--headless")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument('window-size=1920x1080');
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
with open('./Cookie/cookieTestmm.txt','r', newline='')as tmp:
    cookies = json.load(tmp)
driver.get("https://www.tokopedia.com/")
for curcookie in cookies:
    print(curcookie)
    driver.add_cookie(curcookie)
driver.refresh()
#go to messaging
time.sleep(5)
driver.get("https://seller.tokopedia.com/") 
time.sleep(5)
count=0
while True:
    driver.refresh()
    time.sleep(5)
    try:
        countfound=scrapper.get_orderCount(driver.page_source)
        print(countfound)
        if(countfound>count):
            scrapper.sendOrderNotification(countfound)
    except:
        print("connection error")
    time.sleep(15)