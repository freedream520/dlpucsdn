from django.db import models
from django.contrib.auth.models import User
from account.models import department
# Create your models here.
class topic(models.Model):
    auth = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    click = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0,blank=True)
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
