from django.http import response
from django.shortcuts import render
from .sorgu import deneme_function
from django.http import JsonResponse

def home_view_queue(request):
    fatih=deneme_function()
    result=["answer1","answer2","answer3"]
    return JsonResponse({'Answer':result})
    
