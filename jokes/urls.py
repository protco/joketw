from django.conf.urls import url
from django.conf.urls import url, include

from .views import JokeCreateView, JokeUpdateView, JokeDeleteView, JokeUserView


app_name = 'jokes'

urlpatterns = [
    url(r'^jokecreate/', JokeCreateView.as_view(), name='jokecreate'),
    url(r'^(?P<pk>\d+)/jokeupdate/$', JokeUpdateView.as_view(), name='jokeupdate'),
    url(r'^(?P<pk>\d+)/jokedelete/$', JokeDeleteView.as_view(), name='jokedelete'),
    url(r'^jokeusers/', JokeUserView.as_view(), name='jokeusers'),
]
