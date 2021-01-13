from django import forms
from indoorplants.models import Plant

class EditNicknameForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['nickname']
        
class EditWateringForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['watering']
        