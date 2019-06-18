from django.contrib import admin
from .models import Sources

class SourcesAdmin(admin.ModelAdmin):
    list_display=('title_text','pub_date','url_text','rss_text','author_text','created_by','created_on')
    list_filter=['pub_date']
    search_fields=['title_text','url_text','author_text','created_by']
    fieldsets = [
        ('Add Title', {'fields': ['title_text']}),
        ('Date Information', {'fields': ['pub_date']}),
        ('URL Information',  {'fields': ['url_text']}),
        ('RSS Information',  {'fields': ['rss_text']}),
        ('Author Information',  {'fields': ['author_text']}),
        ('Created by', {'fields': ['created_by']}),
        ('Created on', {'fields' : ['created_on']},)
    ]

admin.site.register(Sources, SourcesAdmin)