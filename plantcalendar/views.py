from django.shortcuts import render, reverse, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from datetime import datetime, date
from django.utils.safestring import mark_safe
# from datetime import timedelta
# import calendar
from plantcalendar.models import PlantCalendar, PlantMember
from plantcalendar.utils import Calendar
from plantcalendar.forms import PlantForm, AddPlantForm
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return HttpResponse('hello')


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


class CalendarView(generic.ListView):
    model = PlantCalendar
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


@login_required(login_url='sign_up')
def create_task(request):
    form = PlantForm(request.POST or None)
    if request.POST and form.is_valid():
        plant = form.cleaned_data['plant']
        notes = form.cleaned_data['notes']
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        PlantCalendar.objects.get_or_create(
            user=request.user,
            plant=plant,
            notes=notes,
            start_date=start_date,
            end_date=end_date
        )
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'task.html', {'form': form})


class TaskEdit(generic.UpdateView):
    model = PlantCalendar
    fields = ['plant', 'notes', 'start_date', 'end_date']
    template_name = 'task.html'


def task_details(request, task_id):
    task = PlantCalendar.objects.get(id=task_id)
    plantmember = PlantMember.objects.filter(task=task)
    context = {
        'task': task,
        'plantmember': plantmember
    }
    return render(request, 'task-details.html', context)


def add_plantmember(request, task_id):
    forms = AddPlantForm()
    if request.method == 'POST':
        forms = AddPlantForm(request.POST)
        if forms.is_valid():
            plant = PlantMember.objects.filter(task=task_id)
            task = PlantCalendar.objects.get(id=task_id)
            if plant.count() <= 9:
                user = forms.cleaned_data['user']
                PlantMember.objects.create(
                    task=task,
                    user=user
                )
                return redirect('calendarapp:calendar')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'add_plant.html', context)


class PlantMemberDeleteView(generic.DeleteView):
    model = PlantMember
    template_name = 'task_delete.html'
    success_url = reverse_lazy('calendarapp:calendar')
