import feedparser
from .models import Story
from source.models import Sources

def extract(request):
    model = Sources,Story
    d = feedparser.parse(rss_url)
    for post in d.entries:
        title=post.title
        link=post.link