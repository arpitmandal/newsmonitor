from django.urls import path
from . import views

app_name='story'
urlpatterns = [
# path('add/<int:id>', views.add_story, name='add_story'),
path('story/<int:id>/',views.view_stories, name='story'),
path('newsfeed', views.newsfeed, name='newsfeed'),
]