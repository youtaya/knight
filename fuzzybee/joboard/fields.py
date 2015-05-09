# -*- coding: utf-8 -*-
from django import forms
from joboard.widgets import PlaceMultiWidget

class PlaceMultiField(forms.MultiValueField):
    widget = PlaceMultiWidget

    def __init__(self, *args, **kwargs):
        cities = [(city,city) for city in (u'上海市',u'广州市')]
        districts = [(distrct,distrct) for distrct in (u'浦东新区',u'奉贤区',u'闵行区',u'嘉定区',u'宝山区',u'徐汇区')]
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
