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
    #s = Story(sources=sources,title=title, url=url)

def view_stories(request, id):
    num_post = 15
        # adding stories in database
    try: 
        rss_url = Sources.objects.get(id=id).rss_text
    except Sources.DoesNotExist:
        alert("Does not Exist")
    feed = feedparser.parse(rss_url)
    for post in Story.objects.all():
        post.delete()
    story_urls = Story.objects.filter(id=id).values_list('url', flat=True)
    for entry in feed['entries']:
            url = entry.get('link')
            if url not in story_urls:
                story = Story()
                story.title = entry.get('title')
                story.url = url
                date=entry.get('published')
                story.pub_date = dateutil.parser.parse(date)
                story.body_text = entry.get('description')
                story.save()
    # passing stories data to template context and render it
    context ={
    "id":id
    }
    return render(request, 'story/story_list.html', context)
        #return render(request, "source/story_list.html")

def newsfeed(request):
    return render(request,'story/newsfeed.html')