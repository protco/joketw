# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


GENDER =(('man','Man'),('woman','Woman'))


class UserProfile(models.Model):
    user   = models.OneToOneField(User, null=True, related_name="profile", verbose_name=_(u'User'))
    gender = models.CharField(max_length=40, blank=True, verbose_name=_(u'Gender'), choices=GENDER)
    motto  = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name=_(u'User profile')
        verbose_name_plural = _(u'User profiles')

    def __unicode__(self):
        return u"User profile: %s" % self.user.username

    def get_completion_level(self):
        completion_level = 0
        if self.email_is_verified:
            completion_level += 50
        if self.personal_info_is_completed:
            completion_level += 50
        return completion_level

    def update_completion_level(self):
        self.completion_level = self.get_completion_level()
        self.save()
        return
