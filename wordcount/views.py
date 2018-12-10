from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
from operator import itemgetter

def index(request):
    return render(request, 'base.html', {})

def eggs(request):
    return HttpResponse("<h1>EGGS</h1>")

def count(request):
    fulltext = request.GET['fulltext']
    result = dict(Counter(fulltext.strip().split()))
    result = sorted(result.items(), key = itemgetter(1), reverse = True)
    return render(request, 'count.html', {'result': result})
