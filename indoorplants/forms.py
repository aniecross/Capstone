from django import forms
from indoorplants.models import Plant

class EditNicknameForm(forms.Form):
    nickname = forms.CharField()
        
class EditWateringForm(forms.Form):
    watering = forms.IntegerField()
    
        