from django.forms import ModelForm, Textarea, HiddenInput
from joboard.models import Factory

class FactoryForm(ModelForm):
    class Meta:
        model = Factory
        fields = ['fact_name','fact_addr','fact_lat','fact_lng','hire_num']

        widgets = {
            'fact_name': Textarea(attrs={'cols': 20, 'rows': 2}),
            'fact_addr': Textarea(attrs={'cols': 20, 'rows': 2}),
            'fact_lat': HiddenInput,
            'fact_lng': HiddenInput,
        }
