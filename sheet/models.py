from django.db import models
from django.contrib.auth.models import User
class Sheet(models.Model):
    student = models.CharField(max_length=200)
    present = models.CharField(max_length=200) 
    def __str__(self):
        return self.student


