
def getReply(message):
    res=[]
    for mess in message:
        res.append({'content':mess,'reply':''})
    return res