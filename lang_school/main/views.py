from random import shuffle
import datetime as dt

from django.shortcuts import render

from courses.models import Review


def index(request):
    reviews = list(Review.objects.all())
    shuffle(reviews)
    reviews = reviews[:3]
    
    for review in reviews:
        review.date = f'{review.datetime.day}.{review.datetime.month}.{review.datetime.year}'
        
    context = {'reviews': reviews}
    return render(request, 'main/index.html', context)


def english_course(request):
    context = {}
    return render(request, 'main/english_course.html', context)


def french_course(request):
    context = {}
    return render(request, 'main/french_course.html', context)


def spanish_course(request):
    context = {}
    return render(request, 'main/spanish_course.html', context)


def portfolio(request):
    context = {}
    return render(request, 'main/portfolio.html', context)


def about_project(request):
    context = {}
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {}
    return render(request, 'main/contacts.html', context)


def faq(request):
    context = {}
    return render(request, 'main/faq.html', context)


def test(request):
    context = {}
    return render(request, 'main/test.html', context)
