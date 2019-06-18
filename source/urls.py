from django.urls import path
from . import views

app_name='source'
urlpatterns = [
path('', views.IndexView.as_view(), name='index'),
path('source/<int:pk>', views.DetailView.as_view(), name='detail'),
path('new', views.source_new, name='source_new'),
path('delete/<int:id>', views.source_del, name='source_del'),
]