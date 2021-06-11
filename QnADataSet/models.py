from django.db import models

# Create your models here.
class QnADataSet(models.Model):
    question=models.CharField(max_length=4800)
    answer=models.TextField(max_length=4800)

    def __str__(self):
        return self.question