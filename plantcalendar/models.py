from django.db import models
from django.urls import reverse
from indoorplants.models import PlantType
from myuser.models import MyUser


# Create your models here.
class PlantCalendar(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    plant = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    notes = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plant.name} - {self.user}"

    def get_absolute_url(self):
        return reverse('calendarapp:task-detail', args=(self.id))

    def get_html_url(self):
        url = reverse('calendarapp:task-detail', args=(self))
        return f'<a href="{url}">{self.plant.name}</a>'


class PlantMember(models.Model):
    task = models.ForeignKey(PlantCalendar, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['task', 'user']

    def __str__(self):
        return str(self.user)
