from django.db import models

# Create your models here.


class Topic(models.Model):
    username = models.CharField(max_length=20)
    number = models.IntegerField(max_length=10)
    speciality = models.CharField(max_length=10)
    school = models.CharField(max_length=10)
    email = models.EmailField()
    def __unicode__(self):
        return self.username

