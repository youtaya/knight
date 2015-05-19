# -*- coding: utf-8 -*-
from django import forms
from joboard.widgets import PlaceMultiWidget
import os
from django.conf import settings

class PlaceMultiField(forms.MultiValueField):
    widget = PlaceMultiWidget

    def __init__(self, *args, **kwargs):
        cities = [(city,city) for city in (u'上海市',u'北京市')]

        f = open(os.path.join(settings.BASE_DIR, 'region_sh'))
        districts = [(u'上海市',distrct) for distrct in f.readlines()]

        fields = (
            forms.ChoiceField(choices=cities),
            forms.ChoiceField(choices=districts),
            forms.CharField(),
        )
        super(PlaceMultiField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return ':'.join(data_list)
        return ''

    def to_python(self, value):
        if not value:
            return None
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        return value
