# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from allauth.account.utils import send_email_confirmation
from braces.views import LoginRequiredMixin
from userprofiles.models import UserProfile
from userprofiles.forms import IdentiteForm, EmailForm
from django.contrib.auth.models import User

from stronghold.decorators import public
from stronghold.views import StrongholdPublicMixin

from jokes.models import JokeUser


class ProfileHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofiles/home.html'
    user_check_failure_path = '/comptes/signup/'

    def check_user(self, user):
        if user.is_active:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(ProfileHomeView, self).get_context_data(**kwargs)
        profile = UserProfile.objects.get_or_create(user=self.request.user)[0]
        context['profile'] = profile
        context['profile_self_jokes'] = JokeUser.objects.filter(user=self.request.user).order_by('-created')
        context['profile_self_jokes_num'] = JokeUser.objects.filter(user=self.request.user).count()
        return context


@public
def public_profile(request, username):
    '''
    Display a user's public profile (all the jokes by this user).
    '''
    user = User.objects.get(username=username)
    userprofile = UserProfile.objects.get(user=user)
    user_jokes = JokeUser.objects.filter(user=user).order_by('-created')
    context = {
               'user': user,
               'userprofile': userprofile,
               'user_jokes': user_jokes,
               'joke_count': len(user_jokes)
               }
    return render(request, "userprofiles/public_profile.html", context)










