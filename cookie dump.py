from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json
chrome_options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36' 
chrome_options.add_argument("--disable-logging")  
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument('window-size=1920x1080');

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://www.tokopedia.com/")
while True:
    tmp=input("input \"finish\" after finishing a login >>> ")
    if(tmp=="fin" or tmp=="finish"):
        break
print(driver.get_cookies())

with open('cookieTestmm.txt','w', newline='')as tmp:
    json.dump(driver.get_cookies(), tmp, indent = 6)
driver.close()