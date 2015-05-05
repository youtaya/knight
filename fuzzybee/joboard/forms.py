from django.forms import ModelForm
from joboard.models import Factory

class FactoryForm(ModelForm):
    class Meta:
        model = Factory
        fields = ['fact_name','fact_addr','hire_num']
