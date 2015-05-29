from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Post model
class Post(models.Model):
    date = models.DateTimeField(default=datetime.now)
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User)