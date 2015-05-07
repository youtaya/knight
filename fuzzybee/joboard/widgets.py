from django import forms

class PlaceMultiWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs),
        )
        super(PlaceMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(':')[0:3]
        return ['', '']
