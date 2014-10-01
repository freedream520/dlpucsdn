from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    auth = models.ForeignKey(User)
    title = models.TextField(max_length=100)
    url = models.URLField()
    time_created = models.DateTimeField(auto_now_add=True)
    click = models.IntegerField(default=0)
    class Meta():
        ordering = ['time_created']
    def __unicode__(self):
        return self.title
