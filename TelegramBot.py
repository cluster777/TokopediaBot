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
# bot.send_message(setting["ChatId"], "testing direct Message hooray")
@bot.message_handler(commands=['help', 'start','Start'])
def Send_Welcome(message):
    print(message)
    bot.reply_to(message, "this is hello message")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()