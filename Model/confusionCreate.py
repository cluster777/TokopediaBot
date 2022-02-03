import chatbot
import json
from tensorflow.keras.models import load_model
model = load_model('./Model/chatbot_model.h5')
confusionMatrix=[]

data_file = open('./Model/datasetplusplus.json').read()
intents = json.loads(data_file)
intentsName= [ intent["tag"] for intent in intents["intents"] ]
for intent in intents["intents"]:
    tmpMatrix= {}
    for name in intentsName:
        tmpMatrix[name]=0
    count=0
    for pattern in intent["patterns"]:
        res=(chatbot.predict_class(pattern,model))
        tmpMatrix[res[0]["intent"]]+=1
        count+=1
    for key in tmpMatrix:
        tmpMatrix[key]/=count
    confusionMatrix.append(tmpMatrix)

for i in range(7):
    for j in intentsName:
        print("%.3f" % confusionMatrix[i][j],end=' ')
    print('')
