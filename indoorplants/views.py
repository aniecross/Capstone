from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.views.generic import View

from indoorplants.models import Plant
from journal.models import Entry
from indoorplants.forms import EditPlantForm
# Create your views here.

class PlantView(View):
    def get(self, request, plant_id):
        plant = Plant.objects.get(id=plant_id)
        journal = Entry.objects.filter(plant=plant_id).order_by("created")[::-1]
        return render(request, 'plantdetail.html', {'plant': plant, 'journal': journal})

class LibraryView(View):
    def get(self, request):
        library = Plant.objects.filter(owner=1)
        return render(request, 'plantlibrary.html', {'library': library})
        
@login_required
def edit_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    if request.method == "POST":
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            data = form.cleaned_data
            plant.nickname = data['nickname']
            plant.watering = data['watering']
            plant.save()
            return HttpResponseRedirect(request.GET.get('next', reverse('plant', kwargs={'plant_id': plant.id})))

    form = EditPlantForm(instance=plant)
    return render(request, "generic_form.html", {'form': form, 'plant': plant})

@login_required
def add_plant(request, plant_id):
    me = request.user
    parent_plant = Plant.objects.get(id=plant_id)
    # create an instance of a parent plant with added fields
    new_plant = Plant.objects.create(
        planttype=parent_plant.planttype,
        owner=request.user
    )
    return HttpResponseRedirect(reverse('plant', kwargs={'plant_id': new_plant.id}))

@login_required
def remove_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    plant.delete()
    return HttpResponseRedirect(reverse('homepage'))
