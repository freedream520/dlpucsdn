#coding=utf-8
from django.db import models
from django import forms

class files(models.Model):
    title = models.TextField(blank=True,null=True)
    url = models.URLField()
