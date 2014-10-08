from django.db import models
from django.contrib.auth.models import User
from account.models import department

# Create your models here.

class blogs(models.Model):
    auth = models.ForeignKey(User)
    department_name = models.ForeignKey(department)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)
    click = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    class Meta():
        ordering = ['-time_created']
    def __unicode__(self):
        return self.title

class breply(models.Model):
    auth = models.ForeignKey(User)
    topic = models.ForeignKey(blogs)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    class Meta():
        ordering = ['time_created']
