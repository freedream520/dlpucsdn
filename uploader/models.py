#coding=utf-8
from django.db import models

class file(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True,null=True)

class head(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True,null=True)