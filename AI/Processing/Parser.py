import spacy
nlp = spacy.load("en_core_web_sm")
#Load spacy library
def is_qword(token):
  return token.lower_ in ["who", "what", "where", "when", "why", "how"] and token.dep_ == "attr" or token.dep_ == "advmod"
    #check type of question word

def get_subj_and_obj(sen):
  subjindx = 0
  objindx = 0
  for token in sen:
    #find the nominal subject (nsubj) or passive nominal subject (nsubjpass)
    if "subj" in token.dep_:
      subjindx = token.i 
     #find the direct object (dobj)
    elif "dobj" in token.dep_:
      objindx = token.i 
      #find the object of a preposition (pobj)
    elif "pobj" in token.dep_:
      objindx = token.i 
  return [subjindx,objindx]
  if subjindx == '':
    print("error 1:No Subject")
  if objindx == '':
    print("error 2:No Object")


def search_verbs(PoS_sen):
    num = 0
    lstVerbpos = []
    #for each word in the sentence check if its a verb
    while num < len(PoS_sen):
      if PoS_sen[num] == "VERB":
        #add the verb position to the index
          lstVerbpos.append(num)
      num+=1
    if len(lstVerbpos) == 0:
        print("error 3:No Verb/s")
    return lstVerbpos


def search_nouns(PoS_sen):
  num = 0
  lstNounpos = []
    #for each word in the sentence check if its a noun
  while num < len(PoS_sen):
    if PoS_sen[num] == "NOUN":
    #add the noun position to the index
      lstNounpos.append(num)
    num+=1
  if len(lstNounpos) == 0:
    print("error 4:No Noun/s")
  return lstNounpos


def Type_Of_Sentnce(sen):
    lstSenTypes =[]
    # for every word in the sentence check if its puctuation
    for Token in nlp(sen):
        if Token == 'PUNCT'
        # check the type of puctuation
            if sen[len(sen)-1].text == "?":
                NotComma+=1
                lstSenTypes.append("Q")
            elif sen[len(sen)-1].text == ".":
                NotComma+=1
                lstSenTypes.append("S")
            elif sen[len(sen)-1].text == "!":
                NotComma+=1
                lstSenTypes.append("E")
            elif sen[len(sen)-1].text == ","
                lstSenTypes.append("C")
    if len(lstSenTypes) == 0 or all(word == "," for word in lstSenTypes):
        print("error 5: No proper punctuation")
    return lstSenTypes


def get_sen_structure(text,num):
    from spacy.tokens import Token
    doc = nlp(text)
    #load and tokenize the sentence for pos tagging

    if not Token.has_extension("custom_tag"):
        Token.set_extension("custom_tag", default=None)

    lstPoS = []
    lstOnlyPoS=[]

    for token in doc:
        if token.lower_ in ["hi", "hello", "hey"]:
            token._.custom_tag = "GREET"
        elif token.lower_ in ["who", "what", "where", "when", "why", "how"]:
            token._.custom_tag = "QWORD"
        else:
            token._.custom_tag = token.pos_

        lstPoS.append((token.text, token._.custom_tag))
        lstOnlyPoS.append(token._.custom_tag)
    if num == 1:
      return lstOnlyPoS
    else:
      return lstPoS

def Type_Qword(sen_PoS,indx,sen):
  if indx != -1 and senpos[indx] == "QWORD":
    return sen[indx].text
  else:
    return "No Qword"


def debug_wrd(num,sen):
  SenPoS=get_sen_structure(sen,1)
  print(sen[num],' ',SenPoS[num])

def debug_methods(docs):
  print(docs)
  print(get_sen_structure(docs,1))
  print("Verbs: ",search_verbs(get_sen_structure(docs,1)))
  print("Nouns: ",search_nouns(get_sen_structure(docs,1)))
  print("Type of sentence: ",Type_Of_Sentnce(docs))
  print("Subject : ",(get_subj_And_obj(docs)[0]))
  print("Object : ", (get_subj_And_obj(docs)[1]))
  print("Qword: ",Type_Qword(get_sen_structure(docs,1),get_qword_pos(docs),docs))

def get_qword_pos(sen_text):
    senPoS = get_sen_structure(sen_text, 1)
    for i, tag in enumerate(senPoS):
        if tag == "QWORD":
            return i
    return -1
