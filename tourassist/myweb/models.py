from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user")
    sex = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    birthday = models.DateField()
    avatar = models.ImageField(upload_to= './image/', default='http://tripleami-media.stor.sinaapp.com/image/default.jpg')

class Plan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    starting = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    total_person = models.IntegerField()
    start_time = models.DateField()
    end_time = models.DateField()
    create_time = models.DateField(auto_now=True)

    class Meta:
        #leatest created, nearest start time, nearest end time
        ordering = [ 'start_time', 'end_time','-create_time']

class Team(models.Model):
    master = models.ForeignKey(UserProfile, related_name="master")
    participant = models.ManyToManyField(UserProfile, related_name='participant')
    plan = models.OneToOneField(Plan, related_name="plan")
