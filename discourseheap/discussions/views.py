from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html', context={})

def about(request):
    return render(request, 'welcome.html', context={})

def event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event.html', context={})

def discussion(request, pk):
    #discussion = get_object_or_404(Discussion, pk=pk)

    return render(request, 'discussion.html', context={'discussion_pk':pk})
