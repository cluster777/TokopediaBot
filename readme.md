# Tokopedia Bot # 
A bot program that will chat with your client on tokopedia marketplace

This program have access to telegram to send notification if there is a chat from buyer that it can't answer

## how to use ##

install Python 

install pip

install telebot, beautiful soup, selenium
``` 
pip install pyTelegramBotAPI bs4 selenium webdriver-manager
```
### chromedriver ###
chromedriver no longer required to run the program updated to auto download the requirement and store it in cache

next run "cookie dump.py" and then do login to tokopedia website
> note the cookie only copied into local folder

edit setting_EXAMPLE.json and save it as setting.json
next run TelegramBot.py
> note change the token from the botFather check https://core.telegram.org/bots for detail
> use setting_EXAMPLE.json as baseline

fill chatId with your userID it will direct message there
> chatId use your userId (after running telegram bot it will print on terminal after you click start on the bot chat)

now run cookieImport.py and order.py it will automatically send information to your telegram 
## file explanation ##
here i will explain how each file works
### cookie dump.py ###
in this program it will open new chrome window with tokopedia website in it
we have to do login in this page, after succesfull login **Don't** close it manually but **input** "finish" into the terminal
next the program will take the cookie session on this login session and save it on file named cookieTestmm.json
> do note dont share the cookie with **anyone** with it your login credential can be used 
this program only use selenium to take open the browser session and take the cookie and save it into json using python json module

### cookieImport.py ###
in this program lies the core of the chatbot infrastructure
first the program open tokopedia webpage then load the cookie stored in cookieTestmm.json as it cookie 
next the program open the chat menu of the tokopedia page by clicking on message styled button on the header then click on chat menu (there can be a pin message before this interaction so this program close it first) 
now the program move into the loop to check inbox and wait for message
the big loop
* launch scrapper.py get_Chatcount it will return list of object filled with chatname and chatcount for each
* if there is no chat count it will jump into waiting mode (sleep for 30s then back to loop)
* for each object from get_Chatcount it will open the chat which the chat on and run scrapper.py get_nChat which will return list of last n message object from the chat. 
* for each chat message. the chat message passed into chatbot.py(WIP) which will create a reply for each message if the reply is empty it means it will be passed into telegram chat
* the final step to send the message if the message reply is empty it will call scrapper.py sendChat this will send message using the setting.json token and chatId 
* or it will send into the chat itself by click on chatbox, input the reply, then click the send button
please note several things
> this program need to run using setting.json make it using setting_EXAMPLE.json for the token you can get it from [botfather](https://t.me/botfather) from telegram
> and the chatID from telegrambot.py

### TelegramBot.py ###
the core telegram bot it can do reply "cookieImport message", echo message yup thats all for the moment
first thing to do before starting this program setting the TOKEN yup its the only pre-requisite get it from [botfather](https://t.me/botfather)
from this program it will print its chatId on terminal(maybe i should move it into the chat) input it as the chatId in setting.json

now how this work
* if new start message get in it will throw hello message
* if there is any message it will echo it back
* if user **click** on reply button 
  * it will pop a message teelling to input a reply message
  * then it will send the message using sendReplyMessage.py (TLDR it will do it just like the cookieImport do but only send the message no loop here)
### scrapper.py ###
a set of tool which use beautiful soup to take certain element on website 
here we have 
* get_nChat return N last chat with parameter of (the_site_html,N)
* get_Chatcount return lsit of object {"name","count"} with parameter(the_site_html)
  * name: who send the message 
  * count: how many is the new message
* sendChat send message into telegram with parameter(the_message_itself(string))
in send chat its required to have the setting.json configured since it will take all the other parameter from it

### sendReplyMessage.py ###
read cookieImport for detail
this program works like cookieImport except without loop
open Tokopedia page -> load cookie -> go to chat -> open the chat(using name parameter) -> fill in text area(using message parameter) -> click send -> close itself

### order.py ###
new program to scrap from tokopedia seller page it will send message to telegram if there is new order in the page


### dumpAllChat ###
a program to dump all chat from sender to json file
will only dump message that is string or image or sticker
note may dump unicode
this program used for dataset in this project 

### chatbot.py ###
(WIP)
for now it return empty reply mesage whatever it input is......

have fun 
-- made by cluster777 --