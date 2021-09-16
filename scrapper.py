from bs4 import BeautifulSoup as bs
import re

def get_nChat(target,n):
    soup=bs(target,'html.parser')
    chatBoxAll = soup.find('div', {'class': 'css-1r71t1x'})
    chatHeader = chatBoxAll.findChildren("div" , recursive=False)
    chatAll=chatHeader[2]
    chatAll=chatAll.findChildren("div" , recursive=False)
    return chatAll[-n:]

with open('../tokopedia bot html/Chat _ Tokopedia.html') as f:
    get_nChat(f.read(),2)