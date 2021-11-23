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
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QMainWindow, QApplication
from PyQt5 import uic
import sys
 
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://www.tokopedia.com/")

class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./UI/cookieDump.ui", self)
        self.button = self.findChild(QDialogButtonBox, "finishButton")
        self.accepted.connect(self.acc)
        self.rejected.connect(self.rej)
        self.show()
    def acc(self):
        print("get Cookie")
        print(driver.get_cookies())
        with open('./Cookie/cookieTestmm.txt','w', newline='')as tmp:
            json.dump(driver.get_cookies(), tmp, indent = 6)

        driver.close()
    def rej(self):
        print("exit")
        driver.close()

app = QApplication(sys.argv)
window = UI()
app.exec_()
