# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea, Select, TextInput, HiddenInput
from resume.models import Resume
from django.utils.translation import ugettext_lazy as _

class ResuemForm(ModelForm):
    class Meta:
        model = Resume
