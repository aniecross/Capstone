from django.db import models
from django.urls import reverse
from indoorplants.models import Plant
from myuser.models import MyUser


# Create your models here.
class PlantCalendarEntry(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
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
        if self.plant.nickname:
            return f'<a href="{url}" style="color: #8f6479">{self.plant.nickname}</a>'
        elif self.plant.planttype.common_name:
            return f'<a href="{url}" style="color: #8f6479">{self.plant.planttype.common_name}</a>'
        else:
            return f'<a href="{url}" style="color: #8f6479">{self.plant}</a>'


class PlantWateringEntry(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    entry_date = models.DateField()

    def __str__(self):
        if self.plant.nickname:
            return self.plant.nickname
        else:
            return self.plant.planttype.common_name

    