from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from source.models import Sources
import datetime

class Story(models.Model):
    # Todo use on delete
    sources=models.ManyToManyField(Sources)
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=255)
    pub_date = models.DateTimeField()
    body_text = models.TextField(null=True, blank=True)

class Meta:
    unique_together = ("url", "source")