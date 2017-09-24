# -*- coding: utf-8 -*-

from django import forms
from django.http import Http404
from django.contrib.auth.models import User
from userprofiles.models import UserProfile


class IdentiteForm(forms.ModelForm):
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'gender', 'motto')
        #widgets = {'phone': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super(IdentiteForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
        except User.DoesNotExist:
            raise Http404
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['gender'].required = False
        self.fields['motto'].required = False
        return


class EmailForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
