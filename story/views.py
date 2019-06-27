import feedparser
import datetime
import dateutil.parser
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django_feedparser.settings import *
from .models import Story
from source.models import Sources
from django.utils import timezone
from django.template import loader
from django.db.models.aggregates import Count
from random import randint

def view_stories(request):
    source_id = request.GET('source_id')
    num_post = 20
    args={}
        # adding stories in database
    query_params = {}
    if source_id:
        query_params['id'] = source_id
    source_qs = Sources.objects.filter(**query_params).values('rss_text', 'id')
    for source in source_qs:
        feed = feedparser.parse(source.get('rss_text'))

        story_urls = Story.objects.filter(id=id).values_list('url', flat=True).distinct()
        for entry in feed['entries']:
                url = entry.get('link')
                if url not in story_urls:
                    story = Story()
                    story.title = entry.get('title')
                    story.url = url
                    date=entry.get('published')
                    story.pub_date = dateutil.parser.parse(date)
                    body = entry.get('description')
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(body)
                    body = soup.get_text()
                    story.body_text = body
                    story.source_id = source.get('id')
                    story.save()
    # passing stories data to template context and render it
    args['story']=story
    return render(request, 'story/story_list.html', args)

def newsfeed(request):
    args = {}
    story = Story.objects.all()
    args['story'] = story
    return render(request, 'story/newsfeed.html', args)