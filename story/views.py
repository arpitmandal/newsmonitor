from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Story
from django.utils import timezone
from django.template import loader
from .feed import *


class StoryView(generic.ListView):
    model = Story
    template_name= 'story/story.html'
    
def story(request,id):
    obj = get_object_or_404(Sources,Story,id=id)
    s = Story(sources=sources,title=title, url=url)
    s.save()