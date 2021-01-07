from django import forms
from indoorplants.models import Plant

class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['nickname', 'watering']
        