from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import PlantCalendar


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter task by day
    def formatday(self, day, tasks):
        tasks_per_day = tasks.filter(start_date__day=day)
        d = ''
        for task in tasks_per_day:
            d += f'<li> {task.plant} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, tasks):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, tasks)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter tasks by year and month
    def formatmonth(self, withyear=True):
        tasks = PlantCalendar.objects.filter(
            start_date__year=self.year, start_date__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, tasks)}\n'
        return cal
