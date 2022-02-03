import re
import json
def pre_process(text):
    
    # lowercase
    text=text.lower()
    
    #remove tags
    text=re.sub("[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/#@]","",text)
    
    # string of number and word
    text=re.sub("(\\d|\\W)+"," ",text)
    
    return text
data_file = open('dataSelected.json').read()
sentences= json.loads(open)
#find tf for each sentence
tf=[]
df=[]
frequencyAccumulated={}
for sentence in sentences:
    frequency={}
    terms=sentence.split()
    for term in terms:
        if term in frequency:
            frequency[term]+=1
        else:
            frequency[term]=1
    df.push(frequency)
    tfFound={}
    for key in frequency:
        tfFound[key]=frequency[key]/len(terms)
        if key in frequencyAccumulated:
            frequencyAccumulated[key]+=frequency[key]
        else:
            frequencyAccumulated[key]=frequency[key]
    tf.push(tfFound)

for i in range(len(tf)):
    return 

