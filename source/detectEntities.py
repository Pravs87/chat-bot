import spacy
nlp = spacy.load("en")

# class DetectEntities:
    # nlp = spacy.load("en")

def entities(intent, sentence):
    document = nlp(unicode(sentence))
    labels = set([w.label_ for w in document.ents])
    lists=[]
    for label in labels:
        entities = [cleanup(e.string, lower=False) for e in document.ents if label==e.label_]
        entities = list(set(entities))
        lists.append([label, entities])
        # print label,entities
    base=""
    if intent == 'retrieveEmail':
        base = "Retreiving email with following details: "
    elif intent == 'retrieveDocument':
        base = "Retreiving documents with following details: "
    elif intent == 'call':
        base = "Arranging a call with following details: "
    elif intent == 'scheduleMeeting':
        base = "Scheduling requested meeting with following details: "
    elif intent == 'actionItem':
        base = "Adding an action item with following details: "
    else:
        return intent
    personList = {'PERSON','ORG','GPE'}
    dateList = {'DATE','CARDINAL'}
    for item in lists:
        # print item
        key = item[0]
        value = item[1]

        if str(key) in personList:
            base = base + "People: [ "
            for i in value:
                base = base + str(i) +","
            base = base + "] "
        elif str(key) in dateList:
            base = base + "Date: [ "
            for i in value:
                base = base + str(i) +", "
            base = base + "] "
        elif str(key) == 'TIME':
            base = base + "Time: [ "
            for i in value:
                base = base + str(i) +", "
            base = base + "] "

    if intent == 'retrieveDocument':
        source = retDocument(sentence)
        if source != '':
            base = base+"Source: [ "+source+" ]"
    return base

def cleanup(token, lower = True):
    if lower:
        token = token.lower()
    return token.strip()

def retDocument(sentence):

    keyToken = "from"
    ind = sentence.find(keyToken)
    length = len(sentence)
    source=''
    if ind!=-1 :
        a = sentence.index(' ', ind)
        b = length
        if a < length-1:
            try:
                b = sentence.index(' ', a+1)
            except:
                cc=1
            source = sentence[a+1:b]
    return source