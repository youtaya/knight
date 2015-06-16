# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {
            'username': _(u'用户名/手机号码'),
            'password': _(u'密码'),
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {
            'username': _(u'用户名/手机号码'),
            'password': _(u'密码'),
        }
