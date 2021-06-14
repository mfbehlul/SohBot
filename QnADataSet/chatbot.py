from .models import QnADataSet,greetingsDataSet
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





def greetings(user_input):

    all_greetings = greetingsDataSet.objects.all()
    for q in all_greetings:
        if (q.inputs == "greetings_input"):
            inputs = q.responses
        elif(q.inputs == "greetings_responses"):
            responses = q.responses

    inputs = ast.literal_eval(inputs)
    responses = ast.literal_eval(responses)
    for input in user_input.split():
        if input in inputs:
            return random.choice(responses)


def start_chat(user_input):
    user_input = user_input.lower()
    return greetings(user_input)
