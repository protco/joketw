from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel

from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

from .utils import get_word_count


class Album(TimeStampedModel):
    """Store jokes of different categories: classic vs user """
    title = models.CharField(max_length=50, unique=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class Joke(TimeStampedModel):
    """Regular jokes"""
    album              = models.ForeignKey(Album, default=1, on_delete=models.CASCADE)
    user               = models.ForeignKey(settings.AUTH_USER_MODEL)
    content            = models.TextField(unique=True, blank=False, max_length=500)
    length             = models.PositiveSmallIntegerField(default=0)
    ratings            = GenericRelation(Rating, related_query_name='jokes')
    was_rated_recently = models.BooleanField(default=False)

    def __str__(self):
        return str(self.content)

    def save(self, *args, **kwargs):
        self.length = get_word_count(self.content)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('created',)

class JokeUser(Joke):
    """ jokes submitted by users"""
    is_original        = models.BooleanField(default=False)
    is_flagged         = models.BooleanField(default=False)


class Like(models.Model):
    '''for ajax request of like button'''
    joke = models.ForeignKey(Joke)
