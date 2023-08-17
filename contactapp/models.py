from django.db import models

# Create your models here.
class Contact(models.Model):
       
       Name=models.CharField(max_length=10)
       phoneno=models.BigIntegerField(max_length=20)

      
