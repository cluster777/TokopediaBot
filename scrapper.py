from bs4 import BeautifulSoup as bs
import re
import telebot
from telebot import types

import json
def get_nChat(target,n):
    soup=bs(target,'html.parser')
    chatBoxAll = soup.find('div', {'class': 'css-1r71t1x'})
    chatHeader = chatBoxAll.findChildren("div" , recursive=False)
    chatAll=chatHeader[2]
    chatAll=chatAll.findChildren("div" , recursive=False)
    return chatAll[-n:]

def sendChat(message):
    setting={}
    with open('./setting.json')as f:
        setting=json.load(f)
    API_TOKEN = setting['Token']
    bot = telebot.TeleBot(API_TOKEN)
    # if want to send direct message use this python
    k = types.InlineKeyboardMarkup()
    k.add(types.InlineKeyboardButton("reply", callback_data="reply"))
    bot.send_message(setting["ChatId"], message, reply_markup=k)
