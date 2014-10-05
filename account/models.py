from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User)
    number = models.IntegerField(max_length=10,blank=True)
    identity = models.IntegerField()
    def __unicode__(self):
        return self.user

class department(models.Model):
    name = models.CharField(max_length=5)
    cn = models.TextField(max_length=10)
    def __unicode__(self):
        return self.cn