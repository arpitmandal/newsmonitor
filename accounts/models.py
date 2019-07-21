from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms


class Profile(models.Model):
    username = models.CharField(max_length=200,unique=True)
    birth_date = models.DateField(null=True, blank=True)
    password = models.CharField('Password', max_length=100)
    email = models.EmailField( max_length=100)

