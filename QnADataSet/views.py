from django.http import response
from django.shortcuts import render
from .chatbot import *
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
import json

def start_chatbot(request):
    flag = True
    print("SohBot: Merhaba, benim adım SohBot. Sana nasıl yardımcı olabilirim ?")
    while flag:
        user_input=input("Sen:")
        
        if(user_input !='bye'):
            if (user_input=='teşekkürler' or user_input=='teşekkür ederim'):
                flag=False
                print("SohBot: Rica ederim, yardımcı olmamı istediğin farklı bir konu var mı ?")
            elif (user_input == ""):
                print("Lütfen sorunuzu giriniz.")
            elif (start_chat(user_input)==None):
                print("Ne demek istediğinizi anlayamadım. Lütfen sorunuzu daha açık olarak yazabilir misiniz ?")
            else:
                print("SohBot: " + start_chat(user_input))
                
        else:
            flag=False
            print("SohBot: Bye! Take care.")
    result=["answer1","answer2","answer3"]
    return JsonResponse({'Answer':result})
    

def start_chatting(request):
    response=""
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        message=received_json_data["message"]
        response=start_chat(message)
        
    
    return JsonResponse({'Answer':response})