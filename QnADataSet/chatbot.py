from .models import QnADataSet, greetingsDataSet
import sys
from pathlib import Path
from nltk.chat.util import Chat, reflections
import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import re
from TurkishStemmer import TurkishStemmer


def greetings(user_input):

    all_greetings = greetingsDataSet.objects.all()
    for g in all_greetings:
        if (g.inputs == "greetings_input"):
            inputs = g.responses
        elif(g.inputs == "greetings_responses"):
            responses = g.responses

    inputs = ast.literal_eval(inputs)
    responses = ast.literal_eval(responses)
    for input in user_input.split():
        if input in inputs:
            return random.choice(responses)


# def old_qna_dataset(user_input):

#     data_list=get_dataset_and_list_it()
#     print("Botun cevabı:",response(user_input))
#     for qna in all_qna:
#         question = qna.question
#         answer = qna.answer
#         if (question.find(user_input)) != -1:
#             result.append(qna.answer)

#     if not result:
#         result = None

#     return result

def get_dataset_and_list_it():
    all_qna = QnADataSet.objects.all()
    data=[]#TODO:daha sonra forun içine alınacak
    all_data=[]
    for qna in all_qna:
        
        #data.append(qna.id)
        data.append(qna.question)
        data.append(qna.answer)
        #all_data.append(data)

    #string_data=" ".join([str(item) for item in data])

    #sentence_tokenizer=nltk.sent_tokenize(string_data)
    
    return data



def qna_dataset(user_input):
    db_sentence_list=get_dataset_and_list_it()
    bot_response = ''
    db_sentence_list.append(user_input)
    #print("response un içindeki liste",db_sentence_list)
    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(db_sentence_list)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    print("tfidf",tfidf)
    print("vals",vals)
    print("idx",idx)
    print("flat",flat)
    print("req_tfidf",req_tfidf)

    if(req_tfidf==0):
        bot_response=None
    else:

        if (idx%2==0):
            #if user input is matched with question, bot response get the answer by increasing index
            bot_response = bot_response+db_sentence_list[idx+1]
        else:
            bot_response = bot_response+db_sentence_list[idx]

    
    return bot_response



def get_stem(user_input):
    stemmer=TurkishStemmer()

    #user message is tokenized by word tokenizer
    word_tokenize=nltk.word_tokenize(user_input)
    word_tokenize_stemmed=[]

    #print("kelime listesi:",word_tokenize)
    for i in word_tokenize:
        word_tokenize_stemmed.append(stemmer.stem(i))

 
    stemmed_user_input=" ".join(word_tokenize_stemmed)
    return stemmed_user_input


def daily_conversation(user_input):
    return None


def control_function(user_input):
    # user message is sended to greeting function firstly
    bot_response = greetings(user_input)

    # if user message is not a greeting message, it is sended to daily conversation function
    if (bot_response == None):
        bot_response = daily_conversation(user_input)
        # if user message is not a daily conversation, it is sended to daily qna dataset function
        if (bot_response == None):
            bot_response = qna_dataset(user_input)

    return bot_response

    return None
def start_chat(user_input):
    #user message characters are transformed lowercase
    user_input = user_input.lower()

    #user input is transformed to stems
    user_input_stemmed=get_stem(user_input)
    
    bot_response=control_function(user_input)

    if (bot_response == None):
        bot_response = control_function(user_input_stemmed)
        if (bot_response == None):
            bot_response = "Ne demek istediğinizi anlayamadım. Lütfen sorunuzu daha açık bir şekilde yazabilir misiniz ?"
    return bot_response
