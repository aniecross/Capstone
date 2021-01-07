from django import forms
from journal.models import Entry

       
class JournalEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'photo']