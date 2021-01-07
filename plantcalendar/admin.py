from django.contrib import admin
from plantcalendar.models import PlantCalendar, PlantMember

# Register your models here

class PlantMemberAdmin(admin.ModelAdmin):
    model = PlantMember
    list_display = ['tast', 'user']

admin.site.register(PlantCalendar)
admin.site.register(PlantMember)
