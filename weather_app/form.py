from django.forms import ModelForm,TextInput
from .models import City

class CityForm(ModelForm):
        class Meta:
            model = City
            fields = ['Name']
            widgets = {
                'Name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name','autocomplete':'off'})
            }