# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Coach(models.Model):

    #__Coach_FIELDS__
    coach_name = models.CharField(max_length=255, null=True, blank=True)

    #__Coach_FIELDS__END

    class Meta:
        verbose_name        = _("Coach")
        verbose_name_plural = _("Coach")


class Athlete(models.Model):

    #__Athlete_FIELDS__
    belt_license = models.CharField(max_length=255, null=True, blank=True)

    #__Athlete_FIELDS__END

    class Meta:
        verbose_name        = _("Athlete")
        verbose_name_plural = _("Athlete")


class Provincemaster(models.Model):

    #__Provincemaster_FIELDS__
    province_master = models.CharField(max_length=255, null=True, blank=True)

    #__Provincemaster_FIELDS__END

    class Meta:
        verbose_name        = _("Provincemaster")
        verbose_name_plural = _("Provincemaster")


class Provinceboss(models.Model):

    #__Provinceboss_FIELDS__

    #__Provinceboss_FIELDS__END

    class Meta:
        verbose_name        = _("Provinceboss")
        verbose_name_plural = _("Provinceboss")


class Hirbod(models.Model):

    #__Hirbod_FIELDS__
    confirm = models.CharField(max_length=255, null=True, blank=True)

    #__Hirbod_FIELDS__END

    class Meta:
        verbose_name        = _("Hirbod")
        verbose_name_plural = _("Hirbod")


class Admin(models.Model):

    #__Admin_FIELDS__

    #__Admin_FIELDS__END

    class Meta:
        verbose_name        = _("Admin")
        verbose_name_plural = _("Admin")



#__MODELS__END
