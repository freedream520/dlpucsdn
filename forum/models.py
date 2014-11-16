from django.db import models
from account.models import department
import re
from django.contrib.auth.models import User
# Create your models here.
class node(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.name

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
    yo = models.IntegerField(default=0)
    # node = models.ForeignKey(node,default='all')
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
    yo = models.IntegerField(default=0)
    class Meta():
        ordering = ['time_created']
    def __unicode__(self):
        return str(self.id)+self.topic.title

class mention(models.Model):
    sender = models.ForeignKey(User,related_name='send')
    receiver = models.ForeignKey(User,related_name='receive')
    time_created = models.DateTimeField(auto_now_add=True)
    topic_name = models.ForeignKey(topic,blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    read = models.BooleanField(default=False)
    def __unicode__(self):
        return self.topic_name





