from django.db import models

class Dong(models.Model):
    
    name = models.CharField(max_length=10) #문자열인데 200자가 최대
    
    date = models.DateField('date') #쓴 날짜는 datetime
    
    message = models.TextField()

# Create your models here.
