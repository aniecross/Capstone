from django.db import models
from django.utils import timezone
from myuser.models import MyUser
from indoorplants.models import Plant

# for a journal entry
class Entry(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created = models.DateTimeField(default=timezone.now)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='journalimages/', height_field=None, width_field=None, max_length=None, blank=True, null=True)