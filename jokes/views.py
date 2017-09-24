from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JokeUserSerializer

from .mixins import FormUserNeededMixin, UserOwnerMixin


from .models import JokeUser
from .forms import JokeForm



class JokeCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = JokeForm
    template_name = 'jokes/self_joke_create.html'
    success_url = reverse_lazy("userprofiles:profile-home")


class JokeUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = JokeUser.objects.all()
    form_class = JokeForm
    template_name = 'jokes/self_joke_update.html'
    success_url = reverse_lazy("userprofiles:profile-home")


class JokeDeleteView(LoginRequiredMixin, DeleteView):
    model = JokeUser
    template_name = 'jokes/joke_delete_confirm.html'
    success_url = reverse_lazy("userprofiles:profile-home")


class JokeUserView(APIView):
    """
    API endpoint that allows user-submitted jokes to be accessed.
    """
    def get(self, request):
        jokeusers=JokeUser.objects.all().order_by('-created')
        serializer = JokeUserSerializer(jokeusers, many=True)
        return Response(serializer.data)