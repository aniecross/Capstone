from django import forms
from journal.models import Entry

       
class JournalEntry(forms.Form):
    text = forms.CharField(max_length=300, widget=forms.Textarea)