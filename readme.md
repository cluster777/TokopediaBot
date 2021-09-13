__**Tokopedia Bot**__
A bot program that will chat with your client on tokopedia marketplace

This program have access to telegram to send notification if there is a chat from buyer that it can't answer

how to use

install Python 

install pip

install telebot, beautiful soup, selenium
``` 
pip install pyTelegramBotAPI bs4 selenium
```

download chromedriver from https://chromedriver.chromium.org/downloads
> dont forget **add it to path** named "chromedriver"

next run "cookie dump.py" and then do login to tokopedia website
> note the cookie only copied into local folder

edit setting_EXAMPLE.json and save it as setting.json
next run TelegramBot.py
> note change the token from the botFather check https://core.telegram.org/bots for detail
> use setting_EXAMPLE.json as baseline

fill chatId with your userID it will direct message there
> chatId use your userId (after running telegram bot it will print on terminal after you click start on the bot chat)

now run cookieImport.py it will automatically send information to your telegram 

have fun 

-- made by cluster777 --