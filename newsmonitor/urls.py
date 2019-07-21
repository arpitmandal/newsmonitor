from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('source.urls')),
    path('', include('story.urls')),
    path('', include('accounts.urls')),
]
