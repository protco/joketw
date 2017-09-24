from django.contrib import admin
from django.db import models
from .models import Album, Joke, JokeUser, Like

# Register your models here.
admin.site.register(Album)
admin.site.register(Joke)
admin.site.register(JokeUser)
admin.site.register(Like)


