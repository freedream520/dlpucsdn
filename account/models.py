from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=20)
    number = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)
    def __unicode__(self):
        return self.nickname
