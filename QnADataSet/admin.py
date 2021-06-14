from django.contrib import admin
from .models import QnADataSet,greetingsDataSet
# Register your models here.
admin.site.register(QnADataSet)
admin.site.register(greetingsDataSet)