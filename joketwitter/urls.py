"""joketwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import index, peoplejoke, computerjoke, randomjoke, resources, termofuse, \
                   SearchView, ProfileJokeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^randomjokes/$', randomjoke, name='randomjoke'),
    url(r'^peoplejokes/$', peoplejoke, name='peoplejoke'),
    url(r'^computerjokes/$', computerjoke, name='computerjoke'),
    url(r'^jokesearh/', SearchView.as_view(), name= 'jokesearch'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^jokes/', include('jokes.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^userprofiles/', include('userprofiles.urls')),
    url(r'^contact/',    include('envelope.urls')),
    url(r'^resources/$', resources, name='resources'),
    url(r'^termofuse/$', termofuse, name='termofuse'),
    url(r'profilejoke/', ProfileJokeView.as_view(), name='profilejoke'),
    url(r'^friendship/', include('friendship.urls')),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
