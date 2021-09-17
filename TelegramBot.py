from requests import get

import telebot
from telebot import types
import re
import json
import sendReplyMessage
setting={}
with open('./setting.json')as f:
    setting=json.load(f)
API_TOKEN = setting['Token']
print(API_TOKEN)

bot = telebot.TeleBot(API_TOKEN)

# if want to send direct message use this python
# k = types.InlineKeyboardMarkup()
# k.add(types.InlineKeyboardButton("reply", callback_data="reply"))
# bot.send_message(setting["ChatId"], "the content........ ok insert meme here", reply_markup=k))

@bot.message_handler(commands=['help', 'start','Start'])
def Send_Welcome(message):
    print(message.chat.id)
    bot.reply_to(message, "this is hello message")

@bot.callback_query_handler(func=lambda query: query.data=="reply")
def anotherSendMessage(query):
    print(query)
    msg = {'message':query.message,'value':bot.send_message(query.message.chat.id,"please type message reply this {text} {data}".format(text=query.message.text, data=query.data))}
    bot.register_next_step_handler(msg, fillReply)

def fillReply(message):
    value=message['value']
    source=message['message'].text
    source=re.search('^from (.*)',source).group(1)
    sendReplyMessage.sendReplyMessage(source,value)
    bot.send_message(message.chat.id,"we reply to {source} with {value}".format(source=source,value=value))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()