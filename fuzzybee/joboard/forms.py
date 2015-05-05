from django.forms import ModelForm 
from joboard.models import Factory

class FactoryForm(ModelForm):
    class Meta:
        model = Factory
