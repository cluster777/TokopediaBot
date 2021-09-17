from bs4 import BeautifulSoup as bs
import re
import telebot
from telebot import types

import json
def get_nChat(target,n):
    soup=bs(target,'html.parser')
    chatBoxAll = soup.find('div', {'class': 'css-19idom'})
    chatAll = chatBoxAll.findChildren("div" , recursive=False)
    return chatAll[-n:]

def get_Chatcount(target):
    soup=bs(target,'html.parser')
    chatBoxAll = soup.find_all('div', {'aria-label': 'ChatListItem'})
    res=[]
    for chat in chatBoxAll:
        try:
            # get the name and the chat count
            res.append({'name':chat.find('h3').getText(),'count':chat.find('span').getText()})
        except:
            continue;
    return res
    

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

with open('../tokopedia bot html/Chat Tokopedia + 1 chat .html') as f:
    res=get_Chatcount(f.read())
    for r in res:
        print('------')
        print(r)