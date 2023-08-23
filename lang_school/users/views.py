from datetime import datetime
from calendar import monthrange

from pytz import timezone
from typing import Any, Dict
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.base_user import AbstractBaseUser

from event_calendar.models import EventModel


def user_auth(request):
    context = {}

    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'main/index.html', context)

        context = {'error': 'Username or password not correct'}

    return render(request, 'users/auth.html', context)


def user_logout(request):
    logout(request)
    return redirect('')


def user_profile(request):
    lessons = list(EventModel.objects.filter(student=request.user).all())
    calendar = generate_calendar(lessons)
    print(len([lesson for lesson in lessons if not lesson.is_active]))

    context = {'events': lessons,
               'events_count_done': len([lesson for lesson in lessons if not lesson.is_active]),
               'events_count_total': len(lessons),
               'calendar': calendar
               }
    return render(request, 'users/profile.html', context)


def generate_calendar(lessons: list[EventModel]):
    tzname = 'Europe/Moscow'
    current_cell = 0
    day_idx = 0

    result = '<tr class="table-row"></tr>'
    today = datetime.now(timezone(tzname))
    weekday_start_month = datetime(today.year, today.month, 1).weekday()
    days = monthrange(today.year, today.month)
    days_range = range(days[0], days[1] + 1)

    result += '<tr class="table-row"></tr>'

    for _ in range(weekday_start_month):
        result += '<td class="table-date nil"></td>'
        current_cell += 1

    while True:
        if current_cell == 7:
            current_cell = 0
            result += '</tr><tr class="table-row">'

        try:
            current_day = days_range[day_idx]
        except IndexError:
            result += '</tr>'
            break

        class_name = 'table-date'

        if current_day == today.day:
            class_name += ' active-date'

        for lesson in lessons:

            if lesson.time.day == current_day:
                class_name += ' event-date'

        result += f'<td class="{class_name}">{current_day}</td>'

        current_cell += 1
        day_idx += 1

    return result
