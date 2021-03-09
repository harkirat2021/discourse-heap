from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime

def home(request):
    latest_event = Event.objects.order_by('start_date').first()
    return render(request, 'home.html', context={"event":latest_event})

def about(request):
    return render(request, 'welcome.html', context={})

def event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    messages = Message.objects.filter(event=event)
    return render(request, 'event.html', context={"event":event, "messages":messages})

def get_event_posts(request, pk):
    event = get_object_or_404(Event, pk=pk)
    messages = Message.objects.filter(event=event)

    data = {
        "messages": [model_to_dict(m) for m in messages]
    }
    return JsonResponse(data)

def post_view(request, event_pk):
    if request.POST and request.user.is_authenticated:
        event = get_object_or_404(Event, pk=event_pk)
        discussion = Discussion(event=event, creation_date=datetime.datetime.now())
        discussion.save()
        message = Message(user=request.user, event=event, discussion=discussion, text=request.POST['text'], date=datetime.datetime.now())
        message.save()

        return JsonResponse({"wasPosted": True})
    return JsonResponse({"wasPosted": False})

def discussion(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    messages = Message.objects.filter(discussion=discussion)

    return render(request, 'discussion.html', context={'discussion':discussion, 'messages':messages})
