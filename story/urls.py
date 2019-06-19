from django.urls import path
from . import views

app_name='story'
urlpatterns = [
#path('story/<int:id>', views.StoryView.as_view(), name='story'),
path('story/<int:pk>', views.StoryView.as_view(), name='story'),
]