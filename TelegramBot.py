from bs4 import BeautifulSoup
from requests import get

import telebot
from telebot import types

import json

setting={}
with open('./setting.json')as f:
    setting=json.load(f)
API_TOKEN = setting['Token']
print(API_TOKEN)

bot = telebot.TeleBot(API_TOKEN)

# if want to send direct message use this python
# bot.send_message(setting["ChatId"], "testing direct Message hooray")

@bot.message_handler(commands=['help', 'start','Start'])
def Send_Welcome(message):
    print(message.chat.id)
    k = types.InlineKeyboardMarkup()

    k.add(types.InlineKeyboardButton("reply", callback_data="reply"))
    bot.reply_to(message, "this is hello message", reply_markup=k)

@bot.callback_query_handler(func=lambda query: query.data=="reply")
def anotherSendMessage(query):
    print(query)
    msg = bot.send_message(query.message.chat.id,"please type message reply this {text} {data}".format(text=query.message.text, data=query.data))
    bot.register_next_step_handler(msg, fillReply)

def fillReply(message):
    value=message.text
    bot.send_message(message.chat.id,"we reply with {value}".format(value=value))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()