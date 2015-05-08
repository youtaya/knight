# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets

class PlaceMultiWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        cities = [(city,city) for city in (u'上海市',u'广州市')]
        districts = [(distrct,distrct) for distrct in (u'浦东新区',u'闵行区',u'嘉定区',u'宝山区',u'徐汇区')]
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
