from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User)
    number = models.IntegerField(max_length=10,blank=True)
    def __unicode__(self):
        return self.nickname
