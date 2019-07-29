from django.urls import path
from . import views
from django.conf.urls import url
from . import views as core_views

app_name='accounts'
urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('newuser', views.user_new, name='user_new'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]