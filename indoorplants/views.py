from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.views.generic import View

from indoorplants.forms import EditPlantForm
from indoorplants.models import Plant
from journal.models import Entry
from plantcalendar.models import PlantCalendarEntry
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

            date = datetime.today()
            days = data['watering']
            next_date = date + timedelta(days=days)
            notes = "Time to water edit"
            
            
            PlantCalendarEntry.objects.create(
                owner=plant.owner,
                plant=plant,
                notes=notes,
                entry_date=next_date,
            )


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
    text = f"""A new plant was added to your profile. You can set a custom
        watering schedule/reminder based on your plants actual needs. Don't forget
        to give it a nickname. You can also add your own photos to your journal posts to 
        help you monitor any changes in your plant.... Happy Tracking!!"""
    Entry.objects.create(
        author=me,
        text=text,
        plant=new_plant
    )
    notes = "Time to water"
    date = datetime.today()
    PlantCalendarEntry.objects.create(
        owner=me,
        plant=new_plant,
        notes=notes,
        entry_date=date,
    )
    return HttpResponseRedirect(reverse('plant', kwargs={'plant_id': new_plant.id}))

@login_required
def remove_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    plant.delete()
    return HttpResponseRedirect(reverse('homepage'))
