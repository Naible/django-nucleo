from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


# Post model
class Post(models.Model):
    date = models.DateTimeField(default=datetime.now)
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User)


# Cuisine type model (Many-to-many relationships)
class Cuisine(models.Model):
    cuisine = models.CharField(unique=True, max_length=100)


# Atmosphere type model (Many-to-many relationships)
class Atmosphere(models.Model):
    atmosphere = models.CharField(unique=True, max_length=100)


# Restaurant model
class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    image = models.CharField(max_length=100)
    cuisines = models.ManyToManyField(Cuisine)
    atmospheres = models.ManyToManyField(Atmosphere)


#  UserProfile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    follows = models.ManyToManyField('self', related_name='followed_by',
                                     symmetrical=False)
    favorites = models.ManyToManyField(Restaurant)

    def __unicode__(self):
        return self.user.username
