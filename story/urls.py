from django.urls import path
from . import views

app_name='story'
urlpatterns = [
path('story/<int:id>', Story(), name='story'),
]