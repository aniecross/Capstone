from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import View, ListView

from plantcalendar.models import PlantCalendarEntry
from plantcalendar.utils import Calendar
from plantcalendar.forms import CalEntryForm

import calendar
# Create your views here.

class CalendarView(ListView):
    model = PlantCalendarEntry
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)
        cal.setfirstweekday(firstweekday=6)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
    

class CreateCalEntry(LoginRequiredMixin, View):
    form_class = CalEntryForm

    def get(self, request, entry_id=None):
        if entry_id:
            instance = get_object_or_404(PlantCalendarEntry, pk=entry_id)
        else:
            instance = PlantCalendarEntry()
        form = self.form_class(user=request.user, instance=instance)
        return render(request, 'cal_entry_form.html', {'form': form})

    def post(self, request, entry_id=None):
        if entry_id:
            instance = get_object_or_404(PlantCalendarEntry, pk=entry_id)
            form = self.form_class(request.POST, instance=instance, user=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('calendar'))
        else:
            instance = PlantCalendarEntry()
            form = self.form_class(request.POST, instance=instance, user=request.user)
            if form.is_valid():   
                data = form.cleaned_data
                PlantCalendarEntry.objects.create(
                    owner=request.user,
                    plant=data['plant'],
                    notes=data['notes'],
                    entry_date=data['entry_date'],
                )
                return HttpResponseRedirect(reverse('calendar'))
    
