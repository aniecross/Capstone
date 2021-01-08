from django.contrib import admin
from plantcalendar.models import PlantCalendar

# Register your models here

admin.site.register(PlantCalendar)

# class PlantMemberAdmin(admin.ModelAdmin):
#     model = PlantMember
#     list_display = ['tast', 'user']


# admin.site.register(PlantMember)
