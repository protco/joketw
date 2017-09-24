from django.conf.urls import url
from userprofiles.views import ProfileHomeView, public_profile

app_name = 'userprofiles'
urlpatterns = [
    url(r'^$', ProfileHomeView.as_view(), name='profile-home'),
    url(r'publicprofile/(?P<username>[a-zA-Z0-9]+)/$', public_profile, name='public_profile'),
]
