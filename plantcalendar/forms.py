class PlantForm(ModelForm):
  class Meta:
    model = PlantCalendar
    widgets = {
      'start_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(PlantForm, self).__init__(*args, **kwargs)
    self.fields['start_date'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_date'].input_formats = ('%Y-%m-%dT%H:%M',)