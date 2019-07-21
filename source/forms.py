from django import forms
from .models import Sources
from story.models import Story

class SourceForm(forms.ModelForm):

    class Meta:
        model = Sources
        fields = ('title_text','pub_date','url_text','rss_text','author_text','created_by','created_on')