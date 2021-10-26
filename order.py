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
# chrome_options.add_argument("--headless")
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument('window-size=1920x1080');
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
with open('cookieTestpp.txt','r', newline='')as tmp:
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

a = ActionChains(driver)
m= driver.find_element_by_xpath("//div[@data-testid='btnHeaderInbox']")
a.move_to_element(m).perform()
try:
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='my-shop-container']"))).click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[@href='https://seller.tokopedia.com/home']").click()
except:
    print("ERROR this account is not tokopedia seller account")
time.sleep(5)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
count=0
while True:
    driver.refresh()
    time.sleep(5)
    countfound=scrapper.get_orderCount(driver.page_source)
    print(countfound)
    if(countfound>count):
        scrapper.sendOrderNotification(countfound)
    count=countfound
    time.sleep(15)