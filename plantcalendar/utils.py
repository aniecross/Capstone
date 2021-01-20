from datetime import datetime, timedelta, date
# from calendar import HTMLCalendar
from .models import PlantCalendarEntry, PlantWateringEntry
import calendar

# (firstweekday=6)
class Calendar(calendar.HTMLCalendar):
    def __init__(self, year=None, month=None, request=None): 
        self.year = year
        self.month = month
        self.request = request
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter task by day
    def formatday(self, day, cal_entries, water_entries):
        plants_to_water = water_entries.filter(entry_date__day=day)
        cal_entry_list = cal_entries.filter(entry_date__day=day)
        d = ''
        w = ''
        for entry in plants_to_water:
            w += f'<li>water~{entry.get_html_url} </li>'
        for entry in cal_entry_list:
            d += f'<li> {entry.get_html_url} </li>'
            
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d}{w} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, cal_entries, water_entries):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, cal_entries, water_entries)
        return f'<tr> {week} </tr>'

    # formats a month as a table - add filter to specific user??
    # filter tasks by year and month
    def formatmonth(self, withyear=True):
        water_entries = PlantWateringEntry.objects.filter(
            entry_date__year=self.year, entry_date__month=self.month, owner=self.request.user)
        cal_entries = PlantCalendarEntry.objects.filter(
            entry_date__year=self.year, entry_date__month=self.month, owner=self.request.user)
        # entries = water_entries + cal_entries
        cal = f'<table border="2" cellpadding="3" cellspacing="4" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, cal_entries, water_entries)}\n'
        return cal
