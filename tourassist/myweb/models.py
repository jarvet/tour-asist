from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    sex = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    birthday = models.DateField()

class Plan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_person = models.IntegerField()
    start_time = models.DateField()
    end_time = models.DateField()

class Team(models.Model):
    master = models.OneToOneField(UserProfile, related_name="master")
    participant = models.ManyToManyField(UserProfile, related_name='participant')
    plan = models.OneToOneField(Plan, related_name="plan")