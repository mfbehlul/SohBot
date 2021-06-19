from .models import QnADataSet, greetingsDataSet, dailyConversationDataSet
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
from TurkishStemmer import TurkishStemmer
import numpy as np


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


def daily_conversation(user_input):
    all_dc = dailyConversationDataSet.objects.all()
    for dc in all_dc:
        if (dc.inputs == "daily_conversation_list"):
            responses = dc.responses

    responses = ast.literal_eval(responses)
    for response in responses:
        question = response["question"]

        for q in question:
            if (q.lower().translate(str.maketrans('', '', string.punctuation)) == user_input):
                bot_response = random.choice(response["answer"])
                return bot_response
    return None

def get_dataset_and_list_it():
    all_qna = QnADataSet.objects.all()
    data = [] 
    for qna in all_qna:
        data.append(qna.question)
        data.append(qna.answer)

    return data


def qna_dataset(user_input):
    db_sentence_list = get_dataset_and_list_it()
    bot_response = ''
    db_sentence_list.append(user_input)

    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(db_sentence_list)
    similarity_score = cosine_similarity(tfidf[-1], tfidf)
    index_of_array = similarity_score.argsort()[0][-2]
    flattened_list = similarity_score.flatten()
    flattened_list.sort()
    final_tfidf_score = flattened_list[-2]

    if(final_tfidf_score == 0):
        bot_response = None
    else:
        if (index_of_array % 2 == 0):
            # if user input is matched with question, bot response get the answer by increasing index
            bot_response = bot_response+db_sentence_list[index_of_array+1]
        else:
            bot_response = bot_response+db_sentence_list[index_of_array]

    return bot_response


def get_stem(user_input):
    stemmer = TurkishStemmer()

    # user message is tokenized by word tokenizer
    word_tokenize = user_input.split()
    word_tokenize_stemmed = []

    for i in word_tokenize:
        word_tokenize_stemmed.append(stemmer.stem(i))

    stemmed_user_input = " ".join(word_tokenize_stemmed)
    return stemmed_user_input


def control_function(user_input):
    # user message is sent to greeting function firstly
    bot_response = greetings(user_input)

    # if user message is not a greeting message, it is sent to daily conversation function
    if (bot_response == None):
        bot_response = daily_conversation(user_input)
        # if user message is not a daily conversation, it is sent to qna dataset function
        if (bot_response == None):
            bot_response = qna_dataset(user_input)

    return bot_response


def start_chat(user_input):
    # user message characters are transformed lowercase
    user_input = user_input.lower()

    #all punctuations are removed from user message
    user_input=user_input.translate(str.maketrans('', '', string.punctuation))

    # user input is transformed to stems
    user_input_stemmed = get_stem(user_input)

    bot_response = control_function(user_input)
    if (bot_response == None):
        bot_response = control_function(user_input_stemmed)
        if (bot_response == None):
            bot_response = "Ne demek istediğinizi anlayamadım. Lütfen sorunuzu daha açık bir şekilde yazabilir misiniz ?"
    return bot_response
