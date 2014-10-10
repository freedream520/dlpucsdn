from django.db import models
from account.models import department

# Create your models here.
class departments(models.Model):
    name = models.CharField(max_length=20)
    grade = models.IntegerField()
    college = models.CharField(max_length=20)
    url = models.URLField(blank=True,null=True)
    def __unicode__(self):
        return self.cn