from datetime import datetime
from calendar import monthrange
from pprint import pprint

from pytz import timezone
from typing import Any, Dict
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView

from courses.models import Project
from exercises_words.models import Exercise
from event_calendar.models import EventModel
from users.forms import RegistrationUserForm, CustomPasswordResetForm


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


def user_sign_up(request):
    if request.method == 'GET':
        form = RegistrationUserForm()

    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('')

    context = {'form': form}
    return render(request, 'users/sign_up.html', context)


def user_logout(request):
    logout(request)
    return redirect('')


@login_required
def user_profile(request):
    if request.method == 'POST':
        print(request.POST)
    user_login = request.user

    user = User.objects.filter(username=user_login).first()
    user_is_teacher = user.groups.filter(name='Teacher').exists()
    if user_is_teacher:
        lessons = get_teacher_lessons(user)
        calendar = get_calendar(lessons)

        context = {
            'events': lessons,
            'events_count_total': len(lessons),
            'calendar': calendar
        }
        return render(request, 'users/teacher_profile.html', context)
    else:
        exercises_from_db = list(Exercise.objects.filter(
            student=user_login
        ).all())
        exercises = []

        for ex in exercises_from_db:
            if ex.id not in exercises:
                exercises.append(ex.id)

        lessons = list(EventModel.objects.filter(
            student=user_login).order_by('datetime').all()
        )
        calendar = get_calendar(lessons)
        projects = get_projects(user)

        context = {
            'projects': projects,
            'exercises': exercises,
            'events': lessons,
            'events_count_done': len([lesson for lesson in lessons if lesson.status == 'D']),
            'events_count_total': len(lessons),
            'calendar': calendar
        }
        return render(request, 'users/profile.html', context)


def get_calendar(lessons: list[dict]):
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
            if isinstance(lesson, dict):
                if lesson['datetime'].day == current_day:
                    class_name += ' event-date'
            else:
                if lesson.datetime.day == current_day:
                    class_name += ' event-date'

        result += f'<td class="{class_name}">{current_day}</td>'

        current_cell += 1
        day_idx += 1

    return result


def get_teacher_lessons(user: User):
    lessons = []
    lesson_template = {
        'pk': 0,
        'type': 'personal',  # personal / group,
        'title': 'English',  # English / French / Spanish
        'datetime': None,
        'lessons': EventModel  # EventModel / list[EventModel]
    }

    events_filter = EventModel.objects.filter(teacher=user).all()
    events = [
        EventModel.objects.get(pk=event.pk)
        for event in events_filter
    ]

    for event in events:
        events_datetime = [lesson['datetime'] for lesson in lessons]

        if event.datetime in events_datetime:
            event_idx = events_datetime.index(event.datetime)
            lesson_info = lessons[event_idx]
            lesson_info['type'] = 'group'
            if isinstance(lesson_info['lessons'], list):
                lesson_info['lessons'].append(event)
            else:
                lesson_info['lessons'] = [
                    lesson_info['lessons'], event
                ]
        else:
            lesson_info = lesson_template.copy()
            lesson_info['pk'] = event.pk
            lesson_info['title'] = event.title
            lesson_info['datetime'] = event.datetime
            lesson_info['lessons'] = event
            lessons.append(lesson_info)

    lessons.sort(key=lambda x: x['datetime'])
    return lessons


def get_projects(user: User):
    projects = Project.objects.filter(student=user).all()
    return projects if projects else None


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'users/password_reset_form.html'
    success_url = '/'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    form_class = PasswordResetCompleteView
    template_name = 'users/password_reset_form.html'
    success_url = '/'
