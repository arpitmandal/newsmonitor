import feedparser
import datetime
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
    #s.save()
class StoryView(generic.ListView):
    model = Story
    template_name = 'story_list.html'
    def handle(self,request, id):
        num_post = 15
        try: 
            rss_url = Sources.objects.get(id=id).rss_text
        except Sources.DoesNotExist:
            alert("Does not Exist")
        feed = feedparser.parse(rss_url)
        story_urls = Story.objects.filter(id=id).values_list('url', flat=True)
        for entry in feed['entries']:
                url = entry.get('link')
                if url not in story_urls:
                    story = Story()
                    story.title = entry.get('title')
                    story.url = url
                    story.pub_date = entry.get('published')
                story.save()
        #return render(request, "source/story_list.html")