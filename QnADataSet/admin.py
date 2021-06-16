from django.contrib import admin
from .models import QnADataSet,greetingsDataSet,dailyConversationDataSet
# Register your models here.
admin.site.register(QnADataSet)
admin.site.register(greetingsDataSet)
admin.site.register(dailyConversationDataSet)
