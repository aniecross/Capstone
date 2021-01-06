from django.db import models
from django.utils import timezone
from myuser.models import MyUser

# for a journal entry
class Entry(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created = models.DateTimeField(default=timezone.now)