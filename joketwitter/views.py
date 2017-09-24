from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.views import View
from django.views.generic import ListView
from django.views import generic
from random import sample
from stronghold.decorators import public
from stronghold.views import StrongholdPublicMixin


from jokes.models import Album, Joke, JokeUser, Like
from jokes.forms import JokeForm
from django.contrib.auth.models import User

@public
def index(request):
    '''get top rated jokes for display'''
    #top_ten = Joke.objects.filter(ratings__isnull=False).order_by('-ratings__average')[:20]
    top_ten = Joke.objects.all().order_by('-ratings__average')[:20]
    # get the  newest jokes by user for display
    newest_jokes = JokeUser.objects.order_by('pk').reverse()[:20]

    context = {'title': 'JokeTwitter',
               'newest_jokes': newest_jokes,
               'top_ten': top_ten,
               }
    return render(request, "home.html", context)

@public
def randomjoke(request):
    '''get five random jokes for display'''
    count = Joke.objects.count()
    rand_ids = sample(range(1, count), 50)
    random_five = Joke.objects.filter(id__in=rand_ids)
    print(count, len(random_five), rand_ids)
    context = {'title': 'Random Jokes', 'random_five': random_five}
    return render(request, 'randomjokes.html', context)


@public
def peoplejoke(request):
    people_joke = Joke.objects.filter(content__regex=r'(people)')
    context = {'title': 'People Jokes',
               'people_joke': people_joke,
               }
    return render(request, "peoplejokes.html", context)

@public
def computerjoke(request):
    computer_joke = Joke.objects.filter(content__regex=r'(computer|program)')
    context = {'title': 'Computer Jokes',
               'computer_joke': computer_joke,
               }
    return render(request, "computerjokes.html", context)

@public
def familyjoke(request):
    family_joke = Joke.objects.filter(content__regex=r'(family|grandma|grandpa|father|mother|daughter)')
    context = {'title': 'Family Jokes',
               'family_joke': family_joke,
               }
    return render(request, "familyjokes.html", context)


class SearchView(StrongholdPublicMixin, View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        qs = None
        jokes_num = 0
        if query:
            qs = Joke.objects.filter(Q(content__icontains=query))
            jokes_num = Joke.objects.filter(Q(content__icontains=query)).count()
        context = {'title': 'Search Jokes',
                   'jokes': qs,
                   'jokes_num': jokes_num,
                   }
        return render(request, "search.html", context)


class ProfileJokeView(ListView):
    template_name = 'jokes/profilejokes.html'
    model = JokeUser

    def get_context_data(self, **kwargs):
        context = super(ProfileJokeView, self).get_context_data(**kwargs)
        context['profile_jokes'] = JokeUser.objects.filter(user=self.request.user).order_by('-created')
        context['profile_jokes_num'] = JokeUser.objects.filter(user=self.request.user).count()
        return context

@public
def resources(request):
    context = {'title': 'Resources'}
    return render(request, "resources.html", context)
@public
def termofuse(request):
    context = {'title': 'Term of use'}
    return render(request, "term_of_use.html", context)

