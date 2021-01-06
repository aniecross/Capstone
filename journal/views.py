from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View

from journal.forms import JournalEntry
from journal.models import Entry

# Create your views here.

class CreateEntryView(LoginRequiredMixin, View):
    form_class = JournalEntry
    def get(self, request):
        form = self.form_class()
        return render(request, "generic_form.html", {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Entry.objects.create(
                author=request.user,
                text=data['text']
            )
            return HttpResponseRedirect(reverse('homepage'))

    