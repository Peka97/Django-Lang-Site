from django.shortcuts import render

# Create your views here.


def calendar(request):
    context = {'teacher': False}
    return render(request, 'event_calendar/calendar.html', context)
