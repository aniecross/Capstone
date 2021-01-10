from django import forms
from plantcalendar.models import PlantCalendarEntry
from django.forms import DateInput
from indoorplants.models import Plant


class CalEntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CalEntryForm, self).__init__(*args, **kwargs)
        self.fields['entry_date'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['plant'].queryset = Plant.objects.filter(owner=user)

    class Meta:
        model = PlantCalendarEntry
        widgets = {
          'entry_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        exclude = ['owner']
