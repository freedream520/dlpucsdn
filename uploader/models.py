#coding=utf-8
from django.db import models
from django import forms
from django.contrib.auth.models import User

class files(models.Model):
    auth = models.ForeignKey(User)
    title = models.TextField()
    url = models.URLField(default='')
    upload_time = models.DateTimeField(auto_now_add=True)