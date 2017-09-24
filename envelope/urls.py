# -*- coding: utf-8 -*-

from django.conf.urls import url


from envelope.views import ContactView, thank_you

app_name = 'contact'
urlpatterns = [
    url(r'^$', ContactView.as_view(), name='envelope-contact'),
    url(r'^thankyou$', thank_you, name='thankyou'),
]
