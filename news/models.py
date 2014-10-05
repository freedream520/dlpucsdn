from django.db import models
from django.contrib.auth.models import User
from account.models import department

# Create your models here.
class list(models.Model):
    auth = models.ForeignKey(User)
    title = models.TextField(max_length=100)
    url = models.URLField()
    time_created = models.DateTimeField(auto_now_add=True)
    click = models.IntegerField(default=0)
    department_name = models.ForeignKey(department)
    class Meta():
        ordering = ['-time_created']
    def __unicode__(self):
        return self.title
