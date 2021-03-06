from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from journal.forms import JournalEntry
from journal.models import Entry
from indoorplants.models import Plant

# Create your views here.

class CreateEntryView(LoginRequiredMixin, View):
    form_class = JournalEntry
    def get(self, request, plant_id):
        form = self.form_class()
        return render(request, "generic_form.html", {'form': form})

    def post(self, request, plant_id):
        form = self.form_class(request.POST, request.FILES)
        plant = Plant.objects.get(id=plant_id)
        if form.is_valid():
            data = form.cleaned_data
            Entry.objects.create(
                author=request.user,
                text=data['text'],
                plant=plant,
                photo=data['photo']
            )
            return HttpResponseRedirect(reverse('plant', kwargs={'plant_id': plant_id}))
            
@login_required
def remove_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    plant_id = entry.plant.id
    entry.delete()
    return HttpResponseRedirect(reverse('plant', kwargs={'plant_id': plant_id}))

    
