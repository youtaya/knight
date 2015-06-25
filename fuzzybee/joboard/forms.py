# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea, Select, TextInput, HiddenInput
from joboard.models import Factory
from django.utils.translation import ugettext_lazy as _
from widgets import PlaceMultiWidget

class FactoryForm(ModelForm):
    class Meta:
        model = Factory
        exclude = ('fact_maintainer',)
        fields = ['fact_name','job_position','job_salary','job_gender','fact_addr','fact_lat','fact_lng','hire_num']
        labels = {
            'fact_name': _(u'企业名称'),
            'job_position': _(u'职位类别'),
            'job_salary': _(u'月薪'),
            'job_gender': _(u'性别'),
            'fact_addr': _(u'工作地点'),
            'hire_num': _(u'招聘人数'),
        }
        widgets = {
            'fact_name': Textarea(attrs={'cols': 36, 'rows': 1}),
            'job_position': Select,
            'job_salary': Select,
            'job_gender': Select,
            'fact_addr': PlaceMultiWidget,
            'hire_num': Textarea(attrs={'cols': 10, 'rows': 1}),
            'fact_lat': HiddenInput(attrs={'required': 'False'}),
            'fact_lng': HiddenInput(attrs={'required': 'False'}),
        }
