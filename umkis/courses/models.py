from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    teacher = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    code = models.CharField(max_length=3)
    goals = models.TextField(default='')
    file = models.FileField(upload_to='media', null=True)
