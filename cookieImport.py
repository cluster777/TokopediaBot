from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver = webdriver.Chrome(options=chrome_options)
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

a = ActionChains(driver)
m= driver.find_element_by_xpath("//div[@data-testid='btnHeaderInbox']")
a.move_to_element(m).perform()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/chat']"))).text
driver.find_element_by_xpath("//a[@href='/chat']").click()
time.sleep(5)
driver.save_screenshot("screenshot.png")
while True:
    # remove pin verification notification
    try:
        try:
            driver.find_element_by_xpath("//button[@aria-label='Tutup tampilan modal']").click()
        except:
            print("nothing wrong")
        #the check chat loop
        #check for indicator and get all which have it
        found=scrapper.get_Chatcount(driver.page_source)
        if (found==[]):
            print("no chat found")
            time.sleep(60)
            driver.refresh()
            continue;
        #for each chat with indicator do
        
        for find in found:
            print(find)
            time.sleep(1)
            driver.find_element_by_xpath("//*[text()='{name}']".format(name=find['name'])).click()
            #now chat should be open get the content
            time.sleep(5)
            message=scrapper.get_nChat(driver.page_source,int(find['count']))
            print(message)
            #get the chatbot result for each message
            result=chatbot.getReply(message)

            for chat in result:
                print('-----------')
                print(chat)
                if chat['reply']=='':
                    # send to telegram notification channel for user input
                    print("i send a message to telegram")
                    mess='''from {name} 
                    
                    {content}'''.format(name=find['name'],content=chat['content'])
                    scrapper.sendChat(mess)
                else:
                    #send the message itself
                    textArea=driver.find_element_by_tag_name('textarea')
                    textArea.clear()
                    textArea.send_keys(chat['reply'])
                    time.sleep(1)
                    driver.find_element_by_xpath("//button[@data-testid='btnChatSend']").click()
                    time.sleep(1)
        # ok done wait for next round
        print("round done wait for next")
        time.sleep(30)
        driver.refresh()
        time.sleep(5)
    except Exception as e:
        print("uh error????")
        print(e)
        print("---------^^^^")
        time.sleep(30)
        driver.refresh()
        time.sleep(5)

#while check 
#if there is indicator do reply
#sleep n time