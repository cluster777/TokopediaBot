import telebot
from telebot import types
import re
import json
import os
import Tools.sendReplyMessage as sendReplyMessage
setting={}
try:
    with open('./Telegram/setting.json')as f:
        setting=json.load(f)
except:
    print("file not setting.json not available in this folder please make one dont forget the token")

try:
    API_TOKEN = setting['Token']
except:
    print("Token not yet available please check example for this")
print(API_TOKEN)

try:
    bot = telebot.TeleBot(API_TOKEN)
except:
    print("you got the wrong token please find one with the botfather")

# if want to send direct message use this python
# k = types.InlineKeyboardMarkup()
# k.add(types.InlineKeyboardButton("reply", callback_data="reply"))
# bot.send_message(setting["ChatId"], "the content........ ok insert meme here", reply_markup=k))

@bot.message_handler(commands=['help', 'start','Start'])
def Send_Welcome(message):
    print(message.chat.id)
    bot.reply_to(message, "Hello this is the Tokopedia chatbot we are talking with you in chatId {Id} \nyou can check all the pre-requisite to do by using /check".format(Id=message.chat.id))

@bot.message_handler(commands=['config', 'Config'])
def create_setting(message):
    if setting["ChatId"]=="":
        setting["ChatId"]=message.chat.id
        with open("./Telegram/setting.json","w") as f:
            json.dump(setting, f, indent = 6)
        bot.send_message(message.chat.id,"setting done")
    else:
        bot.send_message(message.chat.id,"there already another chat bound change it into empty string chatid:\"\" ")

    
@bot.message_handler(commands=['Check', 'check'])
def check_Status(message):
    m=""
    if "ChatId" in setting:
        if setting["ChatId"]!=message.chat.id:
            m+="setting not OK use command /config to fix\n"
        else:
            m+="setting OK\n"
    else:
        m+="setting not OK use command /config to fix\n"
    if os.path.isfile('./Cookie/cookieTestmm.txt'):
        m+="cookie ready to use OK\n"
    else:
        m+="cookie not ready use \"cookie dump.py\" to make one"
    bot.send_message(message.chat.id,m)

@bot.callback_query_handler(func=lambda query: query.data=="reply")
def anotherSendMessage(query):

    global mess
    mess=query.message.text
    msg = bot.send_message(query.message.chat.id,"please type message reply this {text} {data}".format(text=query.message.text, data=query.data))
    bot.register_next_step_handler(msg, fillReply)

def fillReply(message):
    value=message.text
    source=mess
    print("**************")
    print(value)
    print("**************")
    print(source)
    source=re.search('from \|\|(.*)\|\|',source).group(1)
    sendReplyMessage.sendReplyMessage(source,value)
    bot.send_message(message.chat.id,"we reply to {source} with {value}".format(source=source,value=value))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()