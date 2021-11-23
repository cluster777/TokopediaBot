# Tokopedia Bot # 
A bot program that will chat with your client on tokopedia marketplace

This program have access to telegram to send notification if there is a chat from buyer that it can't answer

## how to use ##

install Python 

install pip
download the aplication from here by zip or by cloning



install requirements for python
``` 
pip install -r requirements.txt
```
open command prompt into the folder of the aplication

next run "cookie dump.py" and then do login to tokopedia website
> if error no directory or file use this on command prompt(python may work in his directory not in this working directory)
``` 
python "cookie dump.py"
```
> note the cookie only copied into /Cookie folder

open new command prompt in the folder using:
```
start
```
> this will run new cmd in this directory

Get your chatbot Token from https://t.me/botfather
then copy the token into setting_EXAMPLE.json inside /Telegram folder and save it as setting.json

next run TelegramBot.py
> if error no directory or file use this on new command prompt it will stay open and just let it be
``` 
python TelegramBot.py
```
> note change the token from the botFather check https://core.telegram.org/bots for detail
> use setting_EXAMPLE.json as baseline
> you can get token from this by chatting with botFather in this link https://t.me/botfather

after telegramBot running use the link made in botFather and then open it using your telegram then do /config
> this will make the bot send the message there 
> this action can only be done once or when the Telegram/setting.json :chatID set to empty manualy

before running the main program you might like to edit Model/dataset.json file:
>* here contain the reply for each case writen on tag
>* edit the response with the most correct reply for that response
>* example "responses":["a new response"]
>* if you like more than 1 respone do it like "responses":["first response","second response"]
>* you cant sent image or sticker only links or text
>* you can make new line with triple tick for example 
```
```response with newline
new lined response```
```
now run ChatCollector.py and orderCount.py it will automatically send information to your telegram
> if error no directory or file use this on new command prompt it will stay open and just let it be
``` 
python ChatCollector.py
```
```
python orderCount.py
```
## file explanation ##
here i will explain how each file works
### cookie dump.py ###
in this program it will open new chrome window with tokopedia website in it
we have to do login in this page, after succesfull login **Don't** close it manually but click on OK on the newly opened window(dialog) if you want to cancel click on the cancel button on dialog it wont save the cookie if cancel pressed
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
* for each chat message. the chat message passed into chatbot.py which will create a reply for each message if the reply is empty it means it will be passed into telegram chat
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
TLDR it will return the reply when given message array into sendReply

### training.py ###
the one which train the model
create model and store it in the folder of the project there is classes.pkl, chatbot_model.h5 and words.pkl

**note**: the model already pushed so no need to run this

### testingChatbot.py ###
terminal applicatioin to test how the chatbot reply message
input the message in the prompt it will reply back the one chatbot will reply
it call the same module of chatbot.py the one which called in other program


have fun 
-- made by cluster777 --