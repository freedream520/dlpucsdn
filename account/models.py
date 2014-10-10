from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User)
    number = models.IntegerField(max_length=10,blank=True)
    identity = models.IntegerField(default=0)
    website = models.URLField(blank=True,null=True)

    def __unicode__(self):
        return self.user

class department(models.Model):
    name = models.CharField(max_length=5)
    cn = models.TextField(max_length=10)
    def __unicode__(self):
        return self.cn