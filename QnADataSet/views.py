from django.http import response
from django.shortcuts import render
from .chatbot import *
from django.http import JsonResponse
import json


def start_chatting(request):
    response=""
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        message=received_json_data["message"]
        response=start_chat(message)
         
    return JsonResponse({'Answer':response})