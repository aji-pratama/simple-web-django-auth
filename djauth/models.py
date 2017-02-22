from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=30)
    tgl_post = models.DateField(default=timezone.now())
    desc_detail = models.TextField()

class Komentar(models.Model):
    body = models.TextField()
    komentator = models.CharField(max_length=200)
    untuk = models.CharField(max_length=200)
    tgl_post = models.DateField(default=timezone.now())

class Gambar(models.Model):
    nama  = models.CharField(max_length=200)
    gambar = models.CharField(max_length=20000)
