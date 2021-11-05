import chatbot

while True:
    i=input('input any string you like chatbot will reply>')
    arr=[i]
    print(chatbot.getReply(arr)[0])