from django.db import models
from django.contrib.auth.models import User
from account.models import department
import re
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class topic(models.Model):
    auth = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    click = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    last_replied = models.DateTimeField(auto_now_add=True,editable=True)
    deleted = models.BooleanField(default=False)
    department_name = models.ForeignKey(department)
    class Meta():
        ordering = ['-last_replied']
    def __unicode__(self):
        return self.title


class reply(models.Model):
    auth = models.ForeignKey(User)
    topic = models.ForeignKey(topic)
    content = models.TextField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    class Meta():
        ordering = ['time_created']
    def __unicode__(self):
        return str(self.id)+self.topic.title

class mention(models.Model):
    sender = models.ForeignKey(User,related_name='rend')
    receiver = models.ForeignKey(User,related_name='receive')
    time_created = models.DateTimeField(auto_now_add=True)
    mytopic = models.ForeignKey(topic,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    read = models.BooleanField(default=False)
    def __unicode__(self):
        return self.mytopic


