import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../')
import Tools.scrapper as scrapper
print('\n')
with open('chatUnOpened.html') as f:
    r=f.read()
    print('Test scrapper get number of unread chat')
    print(scrapper.get_Chatcount(r))
    print('\n')
    print('Test scrapper get all active chat name')
    print(scrapper.get_allChatname(r))
    print('\n')

with open('chatOpened.html') as f:
    r=f.read()
    print('Test scrapper get n chat get 1 and then 2 then 3')
    print(scrapper.get_nChat(r,1))
    print(scrapper.get_nChat(r,2))
    print(scrapper.get_nChat(r,3))
    print('\n')
    print('Test scrapper get all chat in the chat')
    print(scrapper.get_allchat(r))
    print('\n')
    
with open('sellerDash.html') as f:
    print('Test Scrapper read number of available order')
    print(scrapper.get_orderCount(f.read()))
    print('\n')

with open('sellerDash2.html') as f:
    print('Test Scrapper read number of available order')
    print(scrapper.get_orderCount(f.read()))
    print('\n')
os.chdir('../')
print(os.getcwd())

print('test telegram sending message function')
scrapper.sendChat('''this is test messsage from |me| 
                    and it should be unique from other message''')

print('test telegram send order notification function')
scrapper.sendOrderNotification(1)
scrapper.sendOrderNotification(2)
scrapper.sendOrderNotification(3)

