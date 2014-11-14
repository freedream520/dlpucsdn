from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True,null=True)
    qq = models.IntegerField(max_length=20,blank=True,null=True)
    number = models.IntegerField(max_length=15,blank=True,null=True)
    identity = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    website = models.URLField(default="#")
    head = models.URLField(default='http://dlpucsdn.qiniudn.com/default.png')

    def __unicode__(self):
        return self.user

class department(models.Model):
    name = models.CharField(max_length=5)
    cn = models.CharField(max_length=20)
    def __unicode__(self):
        return self.cn
