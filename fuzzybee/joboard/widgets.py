# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets
import os
from django.conf import settings

class PlaceMultiWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        cities = [(city,city) for city in (u'上海市',u'北京市')]

        f = open(os.path.join(settings.BASE_DIR, 'region_sh'))
        districts = [(u'上海市',distrct) for distrct in f.readlines()]

        _widgets = (
            widgets.Select(attrs=attrs, choices=cities),
            widgets.Select(attrs=attrs, choices=districts),
            widgets.TextInput(attrs=attrs),
        )
        super(PlaceMultiWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.split(':')[0:3]]
        return ['', '', '']

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datalist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        return datalist
