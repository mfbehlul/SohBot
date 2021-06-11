from .models import QnADataSet
import sys
from pathlib import Path

def deneme_function():
    all_qna=QnADataSet.objects.all()
    for i in all_qna:
        print(i)
        print(10*"*")


deneme_function()