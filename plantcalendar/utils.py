from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from .models import PlantCalendarEntry

# (firstweekday=6)
class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None): 
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter task by day
    def formatday(self, day, entries):
        plants_to_water = entries.filter(entry_date__day=day)
        d = ''
        for entry in plants_to_water:
            d += f'<li> {entry.get_html_url} </li>'
            if entry.plant.nickname:
                d += f'<li> {entry.plant.nickname} </li>'
            elif entry.plant.planttype.common_name:
                d += f'<li> {entry.plant.planttype.common_name} </li>'
            else:
                d += f'<li> {entry.plant.planttype.name} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, entries):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, entries)
        return f'<tr> {week} </tr>'

    # formats a month as a table - add filter to specific user??
    # filter tasks by year and month
    def formatmonth(self, withyear=True):
        entries = PlantCalendarEntry.objects.filter(
            entry_date__year=self.year, entry_date__month=self.month)

        cal = f'<table border="2" cellpadding="3" cellspacing="4" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, entries)}\n'
        return cal
