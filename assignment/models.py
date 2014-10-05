from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class assignment(models.Model):
    auth = models.ForeignKey(User)