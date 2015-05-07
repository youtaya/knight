# -*- coding: utf-8 -*-
from django import forms
from joboard.widgets import PlaceMultiWidget

class PlaceMultiField(forms.MultiValueField):
    widget = PlaceMultiWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.ChoiceField(),
            forms.ChoiceField(),
            forms.CharField(),
        )
        super(PlaceMultiField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return ':'.join(data_list)
        return ''
