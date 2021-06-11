from QnADataSet import models
from ..QnADataSet.models import QnADataSet

import sys
def deneme_function():
    all_qna=QnADataSet.objects.all()
    for i in all_qna:
        print(i)
        print(10*"*")
print(sys.path)
deneme_function()
