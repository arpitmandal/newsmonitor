from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Sources(models.Model):
    title_text = models.CharField('Enter Title',max_length=200)
    pub_date = models.DateTimeField('Date Published',default=timezone.now)
    url_text = models.CharField('Enter URL',max_length=200)
    rss_text = models.CharField('Enter RSS',max_length=200)
    author_text = models.CharField('Enter Author Name',max_length=50,null=True)
    created_by = models.CharField('Created By',default=User,max_length=20,null=True)
    created_on = models.DateTimeField('Created on',default=timezone.now)