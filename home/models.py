from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.ForeignKey(User)


class Event(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    notes = models.TextField()
    location = models.CharField(max_length=512)
    meet_date = models.DateTimeField()
    meet_time = models.CharField(max_length=10)
    members = models.ManyToManyField(Member)


class Group(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    description = models.TextField()
    events = models.ManyToManyField(Event, blank=True)
