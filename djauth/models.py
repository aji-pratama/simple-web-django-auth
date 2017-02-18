from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=30)
    desc_detail = models.TextField()

class Komentar(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    komentator = models.CharField(max_length=200)
    untuk = models.CharField(max_length=200)

class Post(models.Model):
    author          = models.ForeignKey('auth.User')
    title           = models.CharField(max_length=200)
    text            = models.TextField()
    created_date    = models.DateTimeField(default=timezone.now())
    published_date  = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
