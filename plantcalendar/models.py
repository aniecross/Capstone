from django.db import models
from django.urls import reverse
from indoorplants.models import Plant
from myuser.models import MyUser

# def my_plant_choices():
#     my_plants = Plant.objects.filter(owner=request.user)

# Create your models here.
class PlantCalendarEntry(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    # entry_for = models.CharField(max_length=100, choices=MY_PLANTS)
    notes = models.TextField(blank=True, null=True)
    entry_date = models.DateField()

    def __str__(self):
        if self.plant.nickname:
            return self.plant.nickname
        else:
            return self.plant.planttype.name

    @property
    def get_html_url(self):
        url = reverse('edit_entry', args=(self.id,))
        return f'<a href="{url}">{self.plant}</a>'

