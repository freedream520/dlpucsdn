from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class topic(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    content = models.TextField()
    click = models.IntegerField()
    time_created = models.DateTimeField()
    last_replied = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    class Meta():
        ordering = ['-last_replied']