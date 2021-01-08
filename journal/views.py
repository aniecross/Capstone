from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import View

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

def custom_404(request):
    return render_to_response(‘404.html’, RequestContext(request))

def custom_500(request):
    return render_to_response(‘404.html’, RequestContext(request))
