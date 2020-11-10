# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

#def welcome(request):
 #   return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date = dt.date.today()
    html = "today is {}-{}-{}".format(date.day, date.month, date.year)
    return HttpResponse(html)

#def past_days_news(request,past_date):
    # Converts data from the string Url
    #date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    #day = convert_dates(date)
    #html = "News for {} {}-{}-{}".format(day, date.day, date.month, date.year)

    #return HttpResponse(html)
from django.shortcuts import render,redirect
#......
# View Function to present news from past days
def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})


def welcome(request):
    return render(request, 'welcome.html')



# Create your views here.
