# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea, TextInput, HiddenInput
from joboard.models import Factory
from django.utils.translation import ugettext_lazy as _
from widgets import PlaceMultiWidget

class FactoryForm(ModelForm):
    class Meta:
        model = Factory
        fields = ['fact_name','fact_addr','fact_lat','fact_lng','hire_num']
        labels = {
            'fact_name': _(u'企业名称'),
            'fact_addr': _(u'工作地点'),
            'hire_num': _(u'招聘人数'),
        }
        widgets = {
            'fact_name': Textarea(attrs={'cols': 40, 'rows': 1}),
            'fact_addr': PlaceMultiWidget,
            'hire_num': Textarea(attrs={'cols': 20, 'rows': 1}),
            'fact_lat': HiddenInput(attrs={'required': 'False'}),
            'fact_lng': HiddenInput(attrs={'required': 'False'}),
        }
